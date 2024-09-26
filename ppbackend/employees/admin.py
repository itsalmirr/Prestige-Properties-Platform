from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Employee model.

    This class customizes the Django admin interface for the Employee model by
    registering it with the admin site and specifying the fields to display in
    the list view.

    Attributes:
        list_display (list): A list of field names to display in the admin list view.
            - "id": The unique identifier for the employee.
            - "full_name": The full name of the employee.
            - "email": The email address of the employee.
            - "role": The role or position of the employee within the organization.
            - "is_mvp": A boolean indicating whether the employee is marked as MVP (Most Valuable Player).
    """

    list_display = ["id", "full_name", "email", "role", "is_mvp"]
