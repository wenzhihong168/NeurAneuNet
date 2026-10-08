import unittest

from neuraneunet.datasets import CaseRecord, DeviceTarget, SplitRole, VolumeSpec
from neuraneunet.evaluation import (
    binary_metrics,
    dice_score,
    mean_absolute_error,
    mean_signed_error,
    percentile_hausdorff,
)
from neuraneunet.models.geometry import (
    cumulative_arc_length,
    interpolate_along_centerline,
    landing_zone_offset,
    project_to_centerline,
)


class SchemaTests(unittest.TestCase):
    def test_case_record_tracks_missing_features(self):
        volume = VolumeSpec((10, 20, 30), (0.5, 0.5, 1.0), "RAS")
        target = DeviceTarget("PED", 4.0, 20.0, 2.0, 3.0)
        record = CaseRecord(
            "case-001",
            SplitRole.TRAIN,
            volume,
            {"age": 60.0, "smoking": None},
            target,
        )
        self.assertEqual(record.missing_clinical_features, ("smoking",))
        self.assertAlmostEqual(volume.voxel_volume_mm3, 0.25)

    def test_invalid_spacing_is_rejected(self):
        with self.assertRaises(ValueError):
            VolumeSpec((10, 10, 10), (1.0, 0.0, 1.0), "RAS")


class MetricTests(unittest.TestCase):
    def test_segmentation_and_binary_metrics(self):
        self.assertAlmostEqual(dice_score([1, 1, 0, 0], [1, 0, 1, 0]), 0.5)
        metrics = binary_metrics([1, 1, 0, 0], [1, 0, 1, 0])
        self.assertAlmostEqual(metrics.sensitivity, 0.5)
        self.assertAlmostEqual(metrics.specificity, 0.5)

    def test_planning_errors_preserve_direction(self):
        self.assertAlmostEqual(mean_absolute_error([4.0, 5.0], [4.5, 4.0]), 0.75)
        self.assertAlmostEqual(mean_signed_error([4.0, 5.0], [4.5, 4.0]), -0.25)

    def test_percentile_hausdorff_uses_physical_points(self):
        left = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)]
        right = [(0.0, 1.0, 0.0), (1.0, 1.0, 0.0)]
        self.assertAlmostEqual(percentile_hausdorff(left, right), 1.0)


class GeometryTests(unittest.TestCase):
    def setUp(self):
        self.centerline = [(0.0, 0.0, 0.0), (3.0, 0.0, 0.0), (3.0, 4.0, 0.0)]

    def test_arc_length_and_interpolation(self):
        self.assertEqual(cumulative_arc_length(self.centerline), (0.0, 3.0, 7.0))
        self.assertEqual(interpolate_along_centerline(self.centerline, 5.0), (3.0, 2.0, 0.0))

    def test_projection_and_landing_offset(self):
        projection = project_to_centerline((2.0, 1.0, 0.0), self.centerline)
        self.assertEqual(projection.point, (2.0, 0.0, 0.0))
        self.assertAlmostEqual(projection.distance_mm, 1.0)
        self.assertAlmostEqual(
            landing_zone_offset((1.0, 0.0, 0.0), (3.0, 2.0, 0.0), self.centerline),
            4.0,
        )


if __name__ == "__main__":
    unittest.main()
