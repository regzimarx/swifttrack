from django.conf.urls import url, include
from . import views
from .views import (
        ProjectManageView, 
        AddProjectView, 
        AssignEmployeeView, 
        EditProjectView,
        EditHoursView,
        RemoveEmployee,
        ReAssignEmployee,
        AdminGlobalSearch,
        AttendanceView,
        AttendanceSearchView
    )

urlpatterns = [
    url(r'^request/create$', views.RequestView.as_view(), name='request'),
    url(r'^request/confirm$', views.UpdateRequest.as_view(), name='update_request'),
    url(r'^dashboard/$', views.AdminView.as_view(), name='admin'),
    url(r'^account/confirm', views.ConfirmAccountView.as_view(), name='confirm_account'),
    url(r'^account/deactivate', views.DeactivateAccountView.as_view(), name='deactivate_account'),
    url(r'^employees/$', views.AllEmployeesView.as_view(), name='all_employees'),
    url(r'^attendance/$', views.AttendanceView.as_view(), name='attendance'),
    url(r'^attendance/search/$', views.AttendanceSearchView.as_view(), name='attendance-search'),
    url(r'^employee/(?P<id>[0-9]+)$', views.EmployeeProfileView.as_view(), name='employee_profile'),
    url(r'^requests/view$', views.ViewRequestsView.as_view(), name='view_all_requests'),
    url(r'^projects/(?P<id>[0-9]+)/$', views.ProjectManageView.as_view(), name='view_projects'),
    url(r'^payroll/$', views.ManagementPayrollView.as_view(), name='management_payroll'),
    url(r'^payroll/update$', views.ManagementPayrollView.as_view(), name='update_payroll'),
    url(r'^add/project/$', AddProjectView.as_view(), name='add_project'),
    url(r'^projects/(?P<id>[0-9]+)/assign/employee/$', AssignEmployeeView.as_view(), name='assign_employee'),
    url(r'^employee/(?P<emp_id>[0-9]+)/reports$', views.ViewReportsByEmployee.as_view(), name='reports_by_employee'),
    url(r'^edit/project/(?P<id>[0-9]+)/$', EditProjectView.as_view(), name='edit-project'),
    url(r'^edit/project/(?P<project_id>[0-9]+)/hours/(?P<id>[0-9]+)/$', EditHoursView.as_view(), name='edit-hours'),
    url(r'^edit/project/(?P<project_id>[0-9]+)/remove/employee/(?P<employee_id>[0-9]+)/$', RemoveEmployee.as_view(), name='remove-employee'),
    url(r'^edit/project/(?P<project_id>[0-9]+)/reassign/employee/(?P<employee_id>[0-9]+)/$', ReAssignEmployee.as_view(), name='reassign-employee'),
    url(r'search/', AdminGlobalSearch.as_view(), name='global-search')
]