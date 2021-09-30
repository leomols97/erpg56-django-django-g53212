from django.test import TestCase
from developer.models import Developer


# Create your tests here.

class Developer(TestCase):
    def test_is_free_with_no_tasks(self):
        """
        is_free() returns True for developer with no
        tasks.
        """
        # dev = Developer.objects.create(first_name="Sébastien", last_name="Drobisz")
        dev = Developer.objects.create(first_name="Sébastien", last_name="Drobisz")
        self.assertIs(True, dev.is_free())

    def test_is_free_with_one_tasks(self):
        """
        is_free() returns False for developer with at least one
        tasks.
        """
        # dev = Developer.objects.create(first_name="Sébastien", last_name="Drobisz")
        dev = Developer.objects.create(first_name="Sébastien", last_name="Drobisz")
        # dev.tasks.create(title="cours Django", description="Faire le cours sur Django")
        dev.tasks.create(title="cours Django", description="Faire le cours sur Django")
        self.assertIs(dev.is_free(), False)
