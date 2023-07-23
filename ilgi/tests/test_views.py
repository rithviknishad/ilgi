from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from users.tests.factories import UserFactory

from ..serializers import (
    CoffeeLogSerializer,
    CoffeeTypeSerializer,
    GoalSerializer,
    MentalHealthLogSerializer,
    MentalHealthSerializer,
    MilestoneRoutineActivityRequirementSerializer,
    MilestoneSerializer,
    RoutineActivityLogSerializer,
    RoutineActivitySerializer,
)
from .factories import (
    CoffeeLogFactory,
    CoffeeTypeFactory,
    GoalFactory,
    MentalHealthFactory,
    MentalHealthLogFactory,
    MilestoneFactory,
    MilestoneRoutineActivityRequirementFactory,
    RoutineActivityFactory,
    RoutineActivityLogFactory,
)


class TestCoffeeLog(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = CoffeeLogFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list CoffeeLog instances"""

        resp = self.client.get("/api/v1/ilgi/coffee-log/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that CoffeeLog collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/ilgi/coffee-log/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve CoffeeLog instances"""

        resp = self.client.get(f"/api/v1/ilgi/coffee-log/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of CoffeeLog can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/ilgi/coffee-log/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new CoffeeLog"""

        resp = self.client.post("/api/v1/ilgi/coffee-log/")
        self.assertEqual(resp.status_code, 403)

    @patch("ilgi.views.CoffeeLogViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for CoffeeLog"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = CoffeeLogSerializer(self.instance).data

        resp = self.client.post("/api/v1/ilgi/coffee-log/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing CoffeeLog"""

        resp = self.client.patch(f"/api/v1/ilgi/coffee-log/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test CoffeeLog update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/ilgi/coffee-log/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete CoffeeLog"""

        resp = self.client.delete(f"/api/v1/ilgi/coffee-log/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test CoffeeLog deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/ilgi/coffee-log/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestCoffeeType(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = CoffeeTypeFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list CoffeeType instances"""

        resp = self.client.get("/api/v1/ilgi/coffee-type/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that CoffeeType collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/ilgi/coffee-type/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve CoffeeType instances"""

        resp = self.client.get(f"/api/v1/ilgi/coffee-type/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of CoffeeType can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/ilgi/coffee-type/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new CoffeeType"""

        resp = self.client.post("/api/v1/ilgi/coffee-type/")
        self.assertEqual(resp.status_code, 403)

    @patch("ilgi.views.CoffeeTypeViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for CoffeeType"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = CoffeeTypeSerializer(self.instance).data

        resp = self.client.post("/api/v1/ilgi/coffee-type/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing CoffeeType"""

        resp = self.client.patch(f"/api/v1/ilgi/coffee-type/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test CoffeeType update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/ilgi/coffee-type/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete CoffeeType"""

        resp = self.client.delete(f"/api/v1/ilgi/coffee-type/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test CoffeeType deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/ilgi/coffee-type/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestGoal(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = GoalFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Goal instances"""

        resp = self.client.get("/api/v1/ilgi/goal/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Goal collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/ilgi/goal/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_list_search(self):
        """Test that Goal collection can be searched by"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            "/api/v1/ilgi/goal/",
            {
                "label__icontains": self.instance.label,
            },
        )
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Goal instances"""

        resp = self.client.get(f"/api/v1/ilgi/goal/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Goal can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/ilgi/goal/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Goal"""

        resp = self.client.post("/api/v1/ilgi/goal/")
        self.assertEqual(resp.status_code, 403)

    @patch("ilgi.views.GoalViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Goal"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = GoalSerializer(self.instance).data

        resp = self.client.post("/api/v1/ilgi/goal/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Goal"""

        resp = self.client.patch(f"/api/v1/ilgi/goal/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Goal update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/ilgi/goal/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Goal"""

        resp = self.client.delete(f"/api/v1/ilgi/goal/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Goal deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/ilgi/goal/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestMentalHealth(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = MentalHealthFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list MentalHealth instances"""

        resp = self.client.get("/api/v1/ilgi/mental-health/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that MentalHealth collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/ilgi/mental-health/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_list_search(self):
        """Test that MentalHealth collection can be searched by"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            "/api/v1/ilgi/mental-health/",
            {
                "label__icontains": self.instance.label,
            },
        )
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve MentalHealth instances"""

        resp = self.client.get(f"/api/v1/ilgi/mental-health/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of MentalHealth can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/ilgi/mental-health/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new MentalHealth"""

        resp = self.client.post("/api/v1/ilgi/mental-health/")
        self.assertEqual(resp.status_code, 403)

    @patch("ilgi.views.MentalHealthViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for MentalHealth"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = MentalHealthSerializer(self.instance).data

        resp = self.client.post("/api/v1/ilgi/mental-health/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing MentalHealth"""

        resp = self.client.patch(f"/api/v1/ilgi/mental-health/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test MentalHealth update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/ilgi/mental-health/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete MentalHealth"""

        resp = self.client.delete(f"/api/v1/ilgi/mental-health/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test MentalHealth deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/ilgi/mental-health/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestMentalHealthLog(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = MentalHealthLogFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list MentalHealthLog instances"""

        resp = self.client.get("/api/v1/ilgi/mental-health-log/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that MentalHealthLog collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/ilgi/mental-health-log/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve MentalHealthLog instances"""

        resp = self.client.get(f"/api/v1/ilgi/mental-health-log/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of MentalHealthLog can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/ilgi/mental-health-log/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new MentalHealthLog"""

        resp = self.client.post("/api/v1/ilgi/mental-health-log/")
        self.assertEqual(resp.status_code, 403)

    @patch("ilgi.views.MentalHealthLogViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for MentalHealthLog"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = MentalHealthLogSerializer(self.instance).data

        resp = self.client.post("/api/v1/ilgi/mental-health-log/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing MentalHealthLog"""

        resp = self.client.patch(
            f"/api/v1/ilgi/mental-health-log/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test MentalHealthLog update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(
            f"/api/v1/ilgi/mental-health-log/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete MentalHealthLog"""

        resp = self.client.delete(f"/api/v1/ilgi/mental-health-log/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test MentalHealthLog deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/ilgi/mental-health-log/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestMilestone(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = MilestoneFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Milestone instances"""

        resp = self.client.get("/api/v1/ilgi/milestone/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Milestone collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/ilgi/milestone/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_list_search(self):
        """Test that Milestone collection can be searched by"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            "/api/v1/ilgi/milestone/",
            {
                "label__icontains": self.instance.label,
            },
        )
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Milestone instances"""

        resp = self.client.get(f"/api/v1/ilgi/milestone/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Milestone can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/ilgi/milestone/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Milestone"""

        resp = self.client.post("/api/v1/ilgi/milestone/")
        self.assertEqual(resp.status_code, 403)

    @patch("ilgi.views.MilestoneViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Milestone"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = MilestoneSerializer(self.instance).data

        resp = self.client.post("/api/v1/ilgi/milestone/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Milestone"""

        resp = self.client.patch(f"/api/v1/ilgi/milestone/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Milestone update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/ilgi/milestone/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Milestone"""

        resp = self.client.delete(f"/api/v1/ilgi/milestone/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Milestone deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/ilgi/milestone/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestMilestoneRoutineActivityRequirement(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = MilestoneRoutineActivityRequirementFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list MilestoneRoutineActivityRequirement instances"""

        resp = self.client.get("/api/v1/ilgi/milestone-routine-activity-requirement/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that MilestoneRoutineActivityRequirement collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/ilgi/milestone-routine-activity-requirement/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_list_filter_exact(self):
        """Test that MilestoneRoutineActivityRequirement collection can be filtered on exact value"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            "/api/v1/ilgi/milestone-routine-activity-requirement/",
            {
                "completed_by_activity__iexact": self.instance.completed_by_activity,
            },
        )
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve MilestoneRoutineActivityRequirement instances"""

        resp = self.client.get(
            f"/api/v1/ilgi/milestone-routine-activity-requirement/{self.instance.id}/"
        )
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of MilestoneRoutineActivityRequirement can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            f"/api/v1/ilgi/milestone-routine-activity-requirement/{self.instance.id}/"
        )

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new MilestoneRoutineActivityRequirement"""

        resp = self.client.post("/api/v1/ilgi/milestone-routine-activity-requirement/")
        self.assertEqual(resp.status_code, 403)

    @patch("ilgi.views.MilestoneRoutineActivityRequirementViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for MilestoneRoutineActivityRequirement"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = MilestoneRoutineActivityRequirementSerializer(
            self.instance
        ).data

        resp = self.client.post(
            "/api/v1/ilgi/milestone-routine-activity-requirement/", {}
        )
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing MilestoneRoutineActivityRequirement"""

        resp = self.client.patch(
            f"/api/v1/ilgi/milestone-routine-activity-requirement/{self.instance.id}/",
            {},
        )
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test MilestoneRoutineActivityRequirement update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(
            f"/api/v1/ilgi/milestone-routine-activity-requirement/{self.instance.id}/",
            {},
        )
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete MilestoneRoutineActivityRequirement"""

        resp = self.client.delete(
            f"/api/v1/ilgi/milestone-routine-activity-requirement/{self.instance.id}/"
        )
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test MilestoneRoutineActivityRequirement deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(
            f"/api/v1/ilgi/milestone-routine-activity-requirement/{self.instance.id}/"
        )

        self.assertEqual(resp.status_code, 204)


class TestRoutineActivity(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = RoutineActivityFactory(owner=self.user)

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list RoutineActivity instances"""

        resp = self.client.get("/api/v1/ilgi/routine-activity/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that RoutineActivity collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/ilgi/routine-activity/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve RoutineActivity instances"""

        resp = self.client.get(f"/api/v1/ilgi/routine-activity/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of RoutineActivity can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/ilgi/routine-activity/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new RoutineActivity"""

        resp = self.client.post("/api/v1/ilgi/routine-activity/")
        self.assertEqual(resp.status_code, 403)

    @patch("ilgi.views.RoutineActivityViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for RoutineActivity"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = RoutineActivitySerializer(self.instance).data

        resp = self.client.post("/api/v1/ilgi/routine-activity/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with(owner=self.user)

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing RoutineActivity"""

        resp = self.client.patch(
            f"/api/v1/ilgi/routine-activity/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test RoutineActivity update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(
            f"/api/v1/ilgi/routine-activity/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete RoutineActivity"""

        resp = self.client.delete(f"/api/v1/ilgi/routine-activity/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test RoutineActivity deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/ilgi/routine-activity/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestRoutineActivityLog(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = RoutineActivityLogFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list RoutineActivityLog instances"""

        resp = self.client.get("/api/v1/ilgi/routine-activity-log/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that RoutineActivityLog collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/ilgi/routine-activity-log/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve RoutineActivityLog instances"""

        resp = self.client.get(f"/api/v1/ilgi/routine-activity-log/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of RoutineActivityLog can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/ilgi/routine-activity-log/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new RoutineActivityLog"""

        resp = self.client.post("/api/v1/ilgi/routine-activity-log/")
        self.assertEqual(resp.status_code, 403)

    @patch("ilgi.views.RoutineActivityLogViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for RoutineActivityLog"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = RoutineActivityLogSerializer(self.instance).data

        resp = self.client.post("/api/v1/ilgi/routine-activity-log/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing RoutineActivityLog"""

        resp = self.client.patch(
            f"/api/v1/ilgi/routine-activity-log/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test RoutineActivityLog update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(
            f"/api/v1/ilgi/routine-activity-log/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete RoutineActivityLog"""

        resp = self.client.delete(
            f"/api/v1/ilgi/routine-activity-log/{self.instance.id}/"
        )
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test RoutineActivityLog deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(
            f"/api/v1/ilgi/routine-activity-log/{self.instance.id}/"
        )

        self.assertEqual(resp.status_code, 204)
