from . import __version__ as app_version

app_name = "tshotel"
app_title = "Tshotel"
app_publisher = "sibi"
app_description = "hotel management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sibikumar@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tshotel/css/tshotel.css"
# app_include_js = "/assets/tshotel/js/tshotel.js"

# include js, css files in header of web template
# web_include_css = "/assets/tshotel/css/tshotel.css"
# web_include_js = "/assets/tshotel/js/tshotel.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tshotel/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tshotel.install.before_install"
# after_install = "tshotel.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tshotel.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
	"Lead":"tshotel.tshotel.custom.Python.contact.Create"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
 	"postal code": {
 		"validate": "tshotel.tshotel.custom.Python.Postcode.post",	
	},
	"Lead": {
 		"validate": "tshotel.tshotel.custom.Python.Postcode.gst",	
	},
	"Lead": {
		"validate":"tshotel.tshotel.custom.Python.Postcode.ph",
	},
#	"Item": {
#		"autoname": "tshotel.tshotel.custom.Python.Postcode.set_si_autoname"
#	}
}

	


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tshotel.tasks.all"
# 	],
# 	"daily": [
# 		"tshotel.tasks.daily"
# 	],
# 	"hourly": [
# 		"tshotel.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tshotel.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tshotel.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tshotel.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tshotel.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tshotel.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tshotel.auth.validate"
# ]

