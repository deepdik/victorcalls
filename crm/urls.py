from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns



router = routers.DefaultRouter()
urlpatterns = [
    path('token', views.login),
    path('Account/token11/', views.Token.as_view()),   # get all , post one
    path('Account/Companies/test', views.CompanyList.as_view()),   # get all , post one

    path('Account/Companies', views.getcmp),   # get all , post one
    path('Account/Company', views.postcmp),   # post one
    path('Account/Company/<int:company_id>', views.Company_company_id_get_update_delete.as_view()),  # GUD operations
    path('Account/integration/companyid/<int:company_id>', views.Integration_of_company.as_view()),
    path('Account/integration/integrationid/<int:integration_id>', views.Integration_by_integrationid.as_view()),
    path('Account/users/', views.AspnetusersList.as_view()),  # get all, post one
    path('account/register', views.post),  # get all, post one
    path('account/user/<str:user_name>/token/<str:token>', views.Add_token.as_view()),
    #path('Account/user/userid/<int:user_id>', views.Aspnetusers_get_update_delete.as_view()),    # GUD operations
    path('Account/User', views.Aspnetusers_update_user.as_view()),    # update user
    #path('Account/Users', views.Aspnetusers_of_company.as_view()),  # get company's users
    path('Account/users/projectid/<int:project_id>', views.users_by_projectid.as_view()),  # get project's users
    #path('Account/users/username/<str:user_name>', views.Aspnetusers_of_username.as_view()),   # get user by user name
    path('Account/user/attendance/<str:date>/<str:username>', views.getattendance.as_view()),
    path('Account/Roles', views.AspnetrolesList.as_view()),  # get all roles, post one
    #path('projects/all/', views.ProjectList.as_view()),    # get all, post one
    #path('Account/projects/userName=<str:user_name>', views.ProjectList.as_view()),    # get all, post one
    path('Account/project/projectid/<int:project_id>', views.Project_project_id_get_update_delete.as_view()),  # GUD operations
    #/api/Account/Projects
    path('account/projects', views.Projects_of_company.as_view()),  # get projects of company
    path('projects/create/', views.Projects_Create.as_view()),  # get projects of company
    path('Account/documents/', views.DocumentsList.as_view()),  # get all, post one
    path('Account/documents/create', views.Cretae_document.as_view()),  # get all, post one
    path('Account/documents/project/<int:project_id>', views.Documents_of_project.as_view()),  # get documents of project
    path('Account/getDocuments/projectid/<int:project_id>', views.Get_project_document.as_view()),  # get project doc
    path('Account/Project/<int:project_id>/Document', views.Documents_of_project_List.as_view()),  # get all, post one
    #path('documents/project/<int:project_id>', views.Documents_of_project_List.as_view()),
    path('Account/document/project/<int:project_id>/<int:document_id>', views.Document_with_projectid_documentid.as_view()),
    path('Account/leads/all/', views.LeadsListAll.as_view()),
    path('Account/leads/id/<int:lead_id>', views.LeadsOneLeads.as_view()),
    #path('leads/cmp/all/<int:company_id>', views.LeadsListAllCmp.as_view()),
    #path('leads/companyid/<int:company_id>/status/<int:status>/pageNum/<int:page_num>', views.LeadsList.as_view()),   # get leads of company
    path('leads/Company/RawLeadsWithPaging', views.Leadsitemss.as_view()),   # get leads of company
    path('Account/getleads/cid/<int:company_id>/status/<int:status_id>', views.LeadsWithStatus.as_view()),   # get leads of company
    path('Account/leads/items/', views.Leads_items_List.as_view()),
    path('Account/recordings/<int:lead_id>', views.Recordingsleadid.as_view()),
    path('Account/recordings/', views.AddRecordings.as_view()),
    path('Account/join/', views.UsersJoinList.as_view()),
    path('Account/join/test/<str:user_name>', views.Aspnetusers_join_aspnetroles.as_view()),
    path('Account/function/test/', views.function_of_postgres.as_view()),
    #path('leads/companyid/statusid/<int:company_id>/<int:status_id>', views.complex_join_of_postgres.as_view()),
    path('Leads/ExcelUpload', views.Upload_excel_file.as_view()),
    path('Leads/leadStatusCounts', views.LeadstatusCountAPIView.as_view()),
    path('Leads', views.OtherLeadsByUsername.as_view()),
    path('Leads/otherC', views.OtherLeadsC.as_view()),
    path('Account/mobile/status/count/companyid/<int:company_id>', views.mobile_status_count),
    path('Account/leads/cretae/companyid/<int:company_id>', views.create_lead),
    #path('leads/update/<int:lead_id>', views.Leads_update_delete.as_view()),
    path('Leads/<int:lead_id>', views.Leads_update),
    path('Account/userroles/', views.AspnetusersWrole.as_view()),
    #path('/api/Account/Users', views.AspnetusersWithrole.as_view()),
    path('Account/Users', views.AspnetusersWithrole.as_view()),
    path('leads/locations',views.locationbyuser.as_view()),
    path('Account/testfilter', views.LeadstatusCountAPIView.as_view()),
    path('Account/test?username=<str:username>', views.gtest),
    path('Leads/LeadsItem', views.LeadItems),

    #Account/

]


urlpatterns = format_suffix_patterns(urlpatterns)



