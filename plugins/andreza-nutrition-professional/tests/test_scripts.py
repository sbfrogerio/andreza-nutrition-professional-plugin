import importlib.util
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1] / "skills"


def load(skill, script):
    path = ROOT / skill / "scripts" / script
    spec = importlib.util.spec_from_file_location(f"{skill}_{script}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ScriptTests(unittest.TestCase):
    def test_diary_preserves_missing_and_groups_dates(self):
        module = load("nutri-analisar-diario-alimentar", "sum_nutrients.py")
        result = module.calculate({"entries": [
            {"date": "2026-09-01", "confidence": "alta", "nutrients": {"energy_kcal": 500, "protein_g": 30}},
            {"date": "2026-09-01", "confidence": "baixa", "nutrients": {"energy_kcal": 400}},
        ]})
        self.assertEqual(result["totals"]["energy_kcal"], 900)
        self.assertEqual(result["coverage"]["protein_g"]["entries_with_value"], 1)
        self.assertFalse(result["missing_values_treated_as_zero"])

    def test_lab_separates_methods(self):
        module = load("nutri-analisar-exames", "lab_trends.py")
        result = module.calculate({"records": [
            {"date": "2026-01-01", "marker": "Ferritina", "value": 30, "unit": "ng/mL", "method": "A"},
            {"date": "2026-02-01", "marker": "Ferritina", "value": 40, "unit": "ng/mL", "method": "B"},
        ]})
        self.assertEqual(len(result["groups"]), 2)
        self.assertFalse(result["different_methods_compared_directly"])

    def test_training_session_rpe(self):
        module = load("nutri-analisar-historico-treinos", "training_history.py")
        result = module.calculate({"sessions": [{"date": "2026-09-01", "duration_min": 60, "srpe": 5}]})
        self.assertEqual(result["weeks"][0]["session_rpe_load"], 300)
        self.assertFalse(result["risk_thresholds_applied"])

    def test_plan_comparison_rejects_invalid_adherence(self):
        module = load("nutri-auditar-planos-anteriores", "compare_plans.py")
        with self.assertRaises(ValueError):
            module.calculate({"plans": [{"name": "A", "adherence_pct": 101}]})

    def test_monitoring_validates_and_calculates_load(self):
        module = load("nutri-monitorar-recuperacao", "summarize_monitoring.py")
        result = module.calculate({"records": [{"date": "2026-09-01", "training_minutes": 45, "srpe": 6}]})
        self.assertEqual(result["metrics"]["session_load"]["mean"], 270)
        self.assertFalse(result["automatic_risk_classification"])

    def test_sweat_rate_formula(self):
        module = load("nutri-planejar-hidratacao-prova", "sweat_rate.py")
        result = module.calculate({"pre_weight_kg": 60, "post_weight_kg": 59.5, "fluid_intake_l": 0.5, "urine_l": 0, "duration_hours": 1})
        self.assertEqual(result["observed_sweat_rate_l_per_hour"], 1.0)
        self.assertFalse(result["clinical_target_selected_by_script"])

    def test_periodization_only_calculates_given_targets(self):
        module = load("nutri-planejar-periodizacao", "calculate_targets.py")
        result = module.calculate({"weight_kg": 60, "days": [{"date": "2026-09-01", "carb_g_per_kg": 5, "protein_g_per_kg": 1.6, "fat_g_per_kg": 1}]})
        self.assertEqual(result["days"][0]["carb_g"], 300)
        self.assertFalse(result["clinical_targets_selected_by_script"])


if __name__ == "__main__":
    unittest.main()

