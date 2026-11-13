# Katalog över docs.zervicepoint.com

Genererad av `scripts/sync_docs.py` 2026-11-13 från 289 sidor. Redigera inte för hand; kör skriptet igen.

Varje rad: sidans titel → leverantörens URL → lokal fulltext i `docs-cache/` (finns efter `python scripts/sync_docs.py`). Raden under en sida listar dess H2/H3-rubriker och fungerar som sökord. Sök med t.ex. `Grep` i `docs-cache/` efter metodnamn eller felkoder.

## Avsnitt

- [Startsida](#startsida) (1)
- [Om dokumentationen](#om-dokumentationen) (1)
- [Introduktion](#introduktion) (3)
- [Kom igång](#kom-igång) (2)
- [Begrepp](#begrepp) (6)
- [Systemöversikt](#systemöversikt) (6)
- [AdminWeb](#adminweb) (18)
- [UserWeb](#userweb) (7)
- [Referens (JavaScript, aktiviteter, formulärfält, snippets)](#referens-javascript-aktiviteter-formulärfält-snippets) (9)
- [Tutorials](#tutorials) (10)
- [How-to (PowerShell, REST, providers m.m.)](#how-to-powershell-rest-providers-mm) (35)
- [Plugins](#plugins) (21)
- [Plugins och malltjänster](#plugins-och-malltjänster) (1)
- [Molnonboarding och worker](#molnonboarding-och-worker) (4)
- [Infrastruktur och installation](#infrastruktur-och-installation) (9)
- [ZerFlow (arbetsflödesmotor)](#zerflow-arbetsflödesmotor) (6)
- [Felsökning](#felsökning) (55)
- [Release notes](#release-notes) (77)
- [Nedladdningar](#nedladdningar) (18)

## Startsida

- **Zervicepoint Documentation** — [/](https://docs.zervicepoint.com/) · [lokal](../docs-cache/index.md)
  - Browse by Task ![🎯](https://cdnjs.cloudflare.com/ajax/libs/emojione/2.2.7/assets/svg/1f3af.svg) · Browse by Role ![🤓](https://cdnjs.cloudflare.com/ajax/libs/emojione/2.2.7/assets/svg/1f913.svg)

## Om dokumentationen

- **Feedback** — [about/feedback/](https://docs.zervicepoint.com/about/feedback/) · [lokal](../docs-cache/about/feedback.md)

## Introduktion

- **Getting started** — [intro/getting-started/](https://docs.zervicepoint.com/intro/getting-started/) · [lokal](../docs-cache/intro/getting-started.md)
- **Next steps** — [intro/nextsteps/](https://docs.zervicepoint.com/intro/nextsteps/) · [lokal](../docs-cache/intro/nextsteps.md)
- **Zervicepoint at a glance** — [intro/zervicepoint-at-a-glance/](https://docs.zervicepoint.com/intro/zervicepoint-at-a-glance/) · [lokal](../docs-cache/intro/zervicepoint-at-a-glance.md)
  - User web · Services · Workflows · Approvals/Tasks · Admin web

## Kom igång

- **Create your own service** — [getting-started/create-your-own-service/](https://docs.zervicepoint.com/getting-started/create-your-own-service/) · [lokal](../docs-cache/getting-started/create-your-own-service.md)
- **Getting started** — [getting-started/getting-started/](https://docs.zervicepoint.com/getting-started/getting-started/) · [lokal](../docs-cache/getting-started/getting-started.md)

## Begrepp

- **Authentication & Authorization** — [concepts/authentication-authorization/](https://docs.zervicepoint.com/concepts/authentication-authorization/) · [lokal](../docs-cache/concepts/authentication-authorization.md)
  - Authentication process · Authorization
- **Understanding the Zervicepoint data train** — [concepts/datatrain/](https://docs.zervicepoint.com/concepts/datatrain/) · [lokal](../docs-cache/concepts/datatrain.md)
  - Overview · ![Workflow](https://docs.zervicepoint.com/images/data-train-workflow-04.png)
- **Integrating with other systems** — [concepts/integration-other-systems/](https://docs.zervicepoint.com/concepts/integration-other-systems/) · [lokal](../docs-cache/concepts/integration-other-systems.md)
  - Integrations in request- and approval forms · Integrations using dynamic drop downs · Dynamic drop down flow · Getting a PowerShell Result using JavaScript · Embedding other Web Systems · Integrations in the workflow · Extending the workflow activity portfolio
- **Multitenant** — [concepts/multitenant/](https://docs.zervicepoint.com/concepts/multitenant/) · [lokal](../docs-cache/concepts/multitenant.md)
- **Order flow** — [concepts/orderflow/](https://docs.zervicepoint.com/concepts/orderflow/) · [lokal](../docs-cache/concepts/orderflow.md)
  - The order flow within Zervicepoint
- **What to consider when building services** — [concepts/servicedesign/](https://docs.zervicepoint.com/concepts/servicedesign/) · [lokal](../docs-cache/concepts/servicedesign.md)
  - Is the whole process known today and does the whole process need to be implemented from the first version · Access · Deeper access control · Option 1 · Option 2 · Self-service or Admin tool · Self-service · Admin services · CRUD · Shared process · All-in-one service or not · Service icons

## Systemöversikt

- **Administration portal (Admin web)** — [system-overview/adminweb/](https://docs.zervicepoint.com/system-overview/adminweb/) · [lokal](../docs-cache/system-overview/adminweb.md)
  - Overview Admin Web · Pages · Page Sections · Tags · Services · Shared Process · Grouped Activities · Providers · Data sources · Slideshow · News · Info blocks · Task log · Orders · Store Settings · Roles · Custom Roles (user Roles) · Translations · E-mail templates · System E-mail Templates
- **System Architecture** — [system-overview/components/](https://docs.zervicepoint.com/system-overview/components/) · [lokal](../docs-cache/system-overview/components.md)
  - Components · User Web · Admin Web · Client Web Service · Provisioning System · Provisioning Inventory System · ProcessSystem Service · Workflow Engine · Service Bus · Database
- **Get to know building blocks** — [system-overview/get-to-know-building-blocks/](https://docs.zervicepoint.com/system-overview/get-to-know-building-blocks/) · [lokal](../docs-cache/system-overview/get-to-know-building-blocks.md)
- **Service** — [system-overview/service/](https://docs.zervicepoint.com/system-overview/service/) · [lokal](../docs-cache/system-overview/service.md)
  - What is a service? · What is a Process? · Service form settings
- **Terminology** — [system-overview/terminology/](https://docs.zervicepoint.com/system-overview/terminology/) · [lokal](../docs-cache/system-overview/terminology.md)
  - Summary · Service · Form · Dynamic forms · Workflow · Variable · Variable List · Parameter · Process · Activity · Data source · Drop Down · Package · Module · Provider · Field · Webservice · Plugin · Shared Process · Example Service · Task · Approval · System Variable · Grouped Activity · Data Train · Page · Tags · Roles · Service List · Service Catalogue · Table · Shared List · Store · Email Template · Task Form · Approval Form · Order · Zervicepoint JavaScript API · Zervicepoint Powershell API
- **End user portal (User web)** — [system-overview/userweb/](https://docs.zervicepoint.com/system-overview/userweb/) · [lokal](../docs-cache/system-overview/userweb.md)
  - Front page · Favourites · Recommended services · Global Search · Info blocks · News · Shopping Cart · Pages · Table pages · Forms · Activity Feed · To-do List · User Profile

## AdminWeb

- **E-mail templates** — [adminweb/emailtemplates/](https://docs.zervicepoint.com/adminweb/emailtemplates/) · [lokal](../docs-cache/adminweb/emailtemplates.md)
  - Overview · System E-mail Templates
- **Grouped Activity** — [adminweb/groupedactivity/](https://docs.zervicepoint.com/adminweb/groupedactivity/) · [lokal](../docs-cache/adminweb/groupedactivity.md)
  - What is a grouped Activities · Creating a grouped activity · Using a grouped activity in a shared process · Updating a grouped activity · Updating from within the linked process · Pushing the updated grouped activity to linked processes
- **Info blocks** — [adminweb/infoblock/](https://docs.zervicepoint.com/adminweb/infoblock/) · [lokal](../docs-cache/adminweb/infoblock.md)
  - Overview
- **News** — [adminweb/news/](https://docs.zervicepoint.com/adminweb/news/) · [lokal](../docs-cache/adminweb/news.md)
  - Overview
- **Order modals** — [adminweb/ordermodals/](https://docs.zervicepoint.com/adminweb/ordermodals/) · [lokal](../docs-cache/adminweb/ordermodals.md)
  - Overview · Order modal info · Using variables in the Title and Body · Button editor · JavaScript Editor
- **Orders** — [adminweb/orders/](https://docs.zervicepoint.com/adminweb/orders/) · [lokal](../docs-cache/adminweb/orders.md)
  - Overview · Events · Tasks · Variables · Restarting an order · Using ZP API to lookup orders
- **Pages** — [adminweb/pages/](https://docs.zervicepoint.com/adminweb/pages/) · [lokal](../docs-cache/adminweb/pages.md)
  - Overview · Page Settings · Page Sections · Text block · Service list · Table
- **Providers and data sources** — [adminweb/providers-and-datasources/](https://docs.zervicepoint.com/adminweb/providers-and-datasources/) · [lokal](../docs-cache/adminweb/providers-and-datasources.md)
  - Overview · Providers · Data sources
- **Roles** — [adminweb/roles/](https://docs.zervicepoint.com/adminweb/roles/) · [lokal](../docs-cache/adminweb/roles.md)
  - Overview · How Roles Work · Role Administration · Create and Manage Roles · Grant Access by Role · Adding Users to a Role · Roles and Data Sources · Dropdown.xml and Shared Modules · Dropdown Configuration · System Roles
- **Sent Emails** — [adminweb/sentemails/](https://docs.zervicepoint.com/adminweb/sentemails/) · [lokal](../docs-cache/adminweb/sentemails.md)
  - Overview · Detailed view · Metadata · Resend email
- **Services** — [adminweb/services/](https://docs.zervicepoint.com/adminweb/services/) · [lokal](../docs-cache/adminweb/services.md)
  - Overview · Service catalog info · Add new service process · Select a process · Enter catalog info · Set page and access · Process Setup · Edit service · Service Versions · Save as copy · Save as draft · Save and publish · View published service
- **Shared Process** — [adminweb/sharedprocess/](https://docs.zervicepoint.com/adminweb/sharedprocess/) · [lokal](../docs-cache/adminweb/sharedprocess.md)
  - Overview · Shared Process settings · Setup Form · Example - Create a Software Group Shared Process · Create a shared process and configure the order form · Configure Setup Form · Configure Workflow · Create service based on shared process · Example - Approval based on checkbox in shared process · Setup form · Process Setup · Workflow · Tutorial
- **Slideshow** — [adminweb/slideshow/](https://docs.zervicepoint.com/adminweb/slideshow/) · [lokal](../docs-cache/adminweb/slideshow.md)
  - Overview
- **Edit Store** — [adminweb/store/](https://docs.zervicepoint.com/adminweb/store/) · [lokal](../docs-cache/adminweb/store.md)
  - Overview · Settings · General · User Authentication · Worker Authentication · E-Mail Settings · Administrative Role · Theme
- **Tags** — [adminweb/tags/](https://docs.zervicepoint.com/adminweb/tags/) · [lokal](../docs-cache/adminweb/tags.md)
  - Overview · How to create a tag · Admin Web · ZP Management API · How to assign a tag to a service · Tags and Service Selector
- **Task log** — [adminweb/tasklog/](https://docs.zervicepoint.com/adminweb/tasklog/) · [lokal](../docs-cache/adminweb/tasklog.md)
  - Overview · How to approve task using Zervicepoint API
- **Users** — [adminweb/users/](https://docs.zervicepoint.com/adminweb/users/) · [lokal](../docs-cache/adminweb/users.md)
  - Overview · Users table info · Users table actions · Temporary users · General fields · If you select "Role Based" · If you select "Specific service" · After you select **Create**
- **Welcome message** — [adminweb/welcomemessage/](https://docs.zervicepoint.com/adminweb/welcomemessage/) · [lokal](../docs-cache/adminweb/welcomemessage.md)
  - Overview · The entry in admin web: · The result in user web: · Welcome message variables

## UserWeb

- **Activity feed** — [userweb/activityfeed/](https://docs.zervicepoint.com/userweb/activityfeed/) · [lokal](../docs-cache/userweb/activityfeed.md)
- **Delegations** — [userweb/delegations/](https://docs.zervicepoint.com/userweb/delegations/) · [lokal](../docs-cache/userweb/delegations.md)
- **Forms** — [userweb/forms/](https://docs.zervicepoint.com/userweb/forms/) · [lokal](../docs-cache/userweb/forms.md)
- **Pages** — [userweb/pages/](https://docs.zervicepoint.com/userweb/pages/) · [lokal](../docs-cache/userweb/pages.md)
  - Landing page · Table pages
- **Self service portal** — [userweb/selfserviceportal/](https://docs.zervicepoint.com/userweb/selfserviceportal/) · [lokal](../docs-cache/userweb/selfserviceportal.md)
- **Services** — [userweb/services/](https://docs.zervicepoint.com/userweb/services/) · [lokal](../docs-cache/userweb/services.md)
  - Favourites · Using the shopping cart feature · Designing service thumbnails:
- **To-do list** — [userweb/todo/](https://docs.zervicepoint.com/userweb/todo/) · [lokal](../docs-cache/userweb/todo.md)

## Referens (JavaScript, aktiviteter, formulärfält, snippets)

- **Activity** — [reference/activity/](https://docs.zervicepoint.com/reference/activity/) · [lokal](../docs-cache/reference/activity.md)
  - Custom Activities · Parameters · Additional Parameters · ParameterSetName "Hidden" · Config Parameter · Output · Output Data types · Prefix · Quickstart - How to create a custom activity · Create a zervicepoint plugin in PowerShell · Create a plugin xml · Trigger Inventory
- **Building blocks** — [reference/building-blocks/](https://docs.zervicepoint.com/reference/building-blocks/) · [lokal](../docs-cache/reference/building-blocks.md)
  - Getting to know your building blocks · Form editor · Explore text fields · Explore the text area · Explore the text block · Explore the drop down list · Drop-down list items · Explore the checkbox · Explore the radio button · Explore the date & time picker · Explore the file upload · Explore the hidden field · Explore the service selector · Explore the form section · Explore the form editor · Workflow editor - Built-in activities · Approval · Set receiver · Task · Set task description · Send e-mail · Assign · Sequence · Conditional sequence · Parallel · While sequence · Code · Delay · Add shared list item · Update shared list item · End workflow
- **Code cookies** — [reference/code-cookies/](https://docs.zervicepoint.com/reference/code-cookies/) · [lokal](../docs-cache/reference/code-cookies.md)
- **Z the Zervicepoint JavaScript API** — [reference/javascript/](https://docs.zervicepoint.com/reference/javascript/) · [lokal](../docs-cache/reference/javascript.md)
  - What is Z API? · Syntax · Selector · Action · Example · Z('#') · Z('form') · length · val() · val(value) · children() · first() · last() · get(index) · disable() · enable() · hide() · show() · toggle(visibility) · visible() · spin(switch, [message]) · valid(valid, message, force) · isValid() · require(require) · add(value, text, isSelected, suppressChange) · clear() · displayName(displayName) · description(description) · getItems() · getItem() · getCategories() · getCategory() · currentUser · currentStore · Actions with function · call()
- **Placeholder** — [reference/placeholder/](https://docs.zervicepoint.com/reference/placeholder/) · [lokal](../docs-cache/reference/placeholder.md)
- **Snippets** — [reference/snippets/](https://docs.zervicepoint.com/reference/snippets/) · [lokal](../docs-cache/reference/snippets.md)
  - What are Snippets? · How do I use them? · Try it out
- **Simple cascading dropdowns** — [reference/snippets/form-cascading-dropdown/](https://docs.zervicepoint.com/reference/snippets/form-cascading-dropdown/) · [lokal](../docs-cache/reference/snippets/form-cascading-dropdown.md)
  - Description · Features · Prerequisites · Zervicepoint version · Configuration needed · How do I use a snippet?
- **Get personal information (Sweden)** — [reference/snippets/form-get-personal-info/](https://docs.zervicepoint.com/reference/snippets/form-get-personal-info/) · [lokal](../docs-cache/reference/snippets/form-get-personal-info.md)
  - Description · Features · Prerequisites · Zervicepoint version · Configuration needed · How do I use a snippet?
- **Multiple approvers from AD group** — [reference/snippets/wf-multiApproveAD/](https://docs.zervicepoint.com/reference/snippets/wf-multiApproveAD/) · [lokal](../docs-cache/reference/snippets/wf-multiApproveAD.md)
  - Description · Features · Prerequisites · Zervicepoint version · Configuration needed · How do I use a snippet?

## Tutorials

- **Create your own activity** — [tutorials/create-custom-activity/](https://docs.zervicepoint.com/tutorials/create-custom-activity/) · [lokal](../docs-cache/tutorials/create-custom-activity.md)
  - Concept · Providers · Data sources · Quickstart · Create a zervicepoint plugin in PowerShell · Create a plugin xml · Trigger Inventory
- **Create your own provider** — [tutorials/create-custom-provider/](https://docs.zervicepoint.com/tutorials/create-custom-provider/) · [lokal](../docs-cache/tutorials/create-custom-provider.md)
  - Concept · Providers · Data sources · Step 1 · Quickstart · Create a zervicepoint plugin in PowerShell · Create a plugin xml · Draft stuff
- **Create a request for support service** — [tutorials/create-request-for-support-service/](https://docs.zervicepoint.com/tutorials/create-request-for-support-service/) · [lokal](../docs-cache/tutorials/create-request-for-support-service.md)
  - Step 1: Create a new Shared process
- **Create your first services** — [tutorials/create-your-first-services/](https://docs.zervicepoint.com/tutorials/create-your-first-services/) · [lokal](../docs-cache/tutorials/create-your-first-services.md)
  - Building your first service · Step 1: Create an initial service · Step 2: View your service · Step 3: Add basic form elements · Step 4: Bind a variable · Step 5: Run your service
- **Data source** — [tutorials/data-source/](https://docs.zervicepoint.com/tutorials/data-source/) · [lokal](../docs-cache/tutorials/data-source.md)
  - Overview · Data Source concepts · Data Source (DropDown) · Search · Validate · GetDefault · GetCategories · Parameters · Data output format · Access Control · Data Source (WebService) · Parameters · Data output format · Access Control · Data Source - Table · Quickstart - Create your first data source · Create the folder structure · Add a PowerShell Module Manifest File(psd1) · Add a 'Search' function to the PowerSell File. (psm1) · Create a provider.xml file · Invoke a new inventory · View data source in Admin Web · Create a service with new data source · Quickstart - Create your first web service
- **Onboard a new colleague** — [tutorials/onboard-new-colleague/](https://docs.zervicepoint.com/tutorials/onboard-new-colleague/) · [lokal](../docs-cache/tutorials/onboard-new-colleague.md)
- **Onboarding** — [tutorials/onboarding/](https://docs.zervicepoint.com/tutorials/onboarding/) · [lokal](../docs-cache/tutorials/onboarding.md)
  - Introduction · Zervicepoint Topology · Zervicepoint Roles · Authentication · Run zervicepoint installer · Ports & Traffic flow · Checklist
- **Software License Shared Process** — [tutorials/scenario-test/](https://docs.zervicepoint.com/tutorials/scenario-test/) · [lokal](../docs-cache/tutorials/scenario-test.md)
  - Goal · Add Page · Create Shared Process · Update Role · Add service based on Shared Process
- **Work with translation variables** — [tutorials/work-with-translation-variables/](https://docs.zervicepoint.com/tutorials/work-with-translation-variables/) · [lokal](../docs-cache/tutorials/work-with-translation-variables.md)
  - Step 1: Create an empty service · Step 2: Create a translation variable · Step 3: Create a new activity that supports translation variables · Step 4: Create a simple workflow with the new activity · Step 5: Order the service
- **Working with variables** — [tutorials/work-with-variables/](https://docs.zervicepoint.com/tutorials/work-with-variables/) · [lokal](../docs-cache/tutorials/work-with-variables.md)
  - Learn how to make use of variables in your services · Step 1: Combine variables · Step 2: Create a Request for support service

## How-to (PowerShell, REST, providers m.m.)

- **Check for errors in workflow instance** — [how-to/how-to-check-errors-in-workflow-status-details-for-order-in-queue-state/](https://docs.zervicepoint.com/how-to/how-to-check-errors-in-workflow-status-details-for-order-in-queue-state/) · [lokal](../docs-cache/how-to/how-to-check-errors-in-workflow-status-details-for-order-in-queue-state.md)
  - Step-by-step guide
- **Clear test orders from an installation before go-live** — [how-to/how-to-clear-test-orders-from-a-zervicepoint-installation-before-go-live/](https://docs.zervicepoint.com/how-to/how-to-clear-test-orders-from-a-zervicepoint-installation-before-go-live/) · [lokal](../docs-cache/how-to/how-to-clear-test-orders-from-a-zervicepoint-installation-before-go-live.md)
- **Setup Role for MFA users** — [how-to/how-to-create-MFA-role/](https://docs.zervicepoint.com/how-to/how-to-create-MFA-role/) · [lokal](../docs-cache/how-to/how-to-create-MFA-role.md)
  - Create the Role · Extra step for On-premise installations
- **Create and manage stores** — [how-to/how-to-create-and-manage-stores-with-zervicepoint-powershell-management/](https://docs.zervicepoint.com/how-to/how-to-create-and-manage-stores-with-zervicepoint-powershell-management/) · [lokal](../docs-cache/how-to/how-to-create-and-manage-stores-with-zervicepoint-powershell-management.md)
  - Introduction · Retrieving information about a store · Creating a new store from scratch · Creating a new store based on an existing store · Creating a new store and cloning the content of an existing store · Updating an existing store · Deleting a store
- **Erase personal data** — [how-to/how-to-erase-personally-identifiable-information-in-accordance-with-gdpr/](https://docs.zervicepoint.com/how-to/how-to-erase-personally-identifiable-information-in-accordance-with-gdpr/) · [lokal](../docs-cache/how-to/how-to-erase-personally-identifiable-information-in-accordance-with-gdpr.md)
  - Clear-ZPUserProfile · Get-ZPOrderParameter · Clear-ZPOrderParameter · Clear-ZPOrder · Erasing data from order parameters · Erasing entire orders · Erasing data from a user's profile
- **Export and import services** — [how-to/how-to-export-and-import-services-with-zervicepoint-powershell-management/](https://docs.zervicepoint.com/how-to/how-to-export-and-import-services-with-zervicepoint-powershell-management/) · [lokal](../docs-cache/how-to/how-to-export-and-import-services-with-zervicepoint-powershell-management.md)
  - Exporting a service and its associated process · Importing a service and process
- **Use file form element or email activity file attachments** — [how-to/how-to-file-upload-api/](https://docs.zervicepoint.com/how-to/how-to-file-upload-api/) · [lokal](../docs-cache/how-to/how-to-file-upload-api.md)
  - Goal · Scenario 1 - File upload · Create Service · Place test order · Scenario 2 - Email file attachment · Before you begin · Create Order Form · Create Activity to export file · Update workflow to export agreement · Update workflow Send manual to requester
- **Find token signing thumbprint** — [how-to/how-to-find-adfs-thumbprint/](https://docs.zervicepoint.com/how-to/how-to-find-adfs-thumbprint/) · [lokal](../docs-cache/how-to/how-to-find-adfs-thumbprint.md)
- **Find processes with DOM-manipulations** — [how-to/how-to-find-processes-with-dom-manipulations-and-export-to-excel/](https://docs.zervicepoint.com/how-to/how-to-find-processes-with-dom-manipulations-and-export-to-excel/) · [lokal](../docs-cache/how-to/how-to-find-processes-with-dom-manipulations-and-export-to-excel.md)
  - Step-by-step guide · Columns and explanations · Common DOM-manipulations
- **Get started with REST API** — [how-to/how-to-get-started-with-rest-api/](https://docs.zervicepoint.com/how-to/how-to-get-started-with-rest-api/) · [lokal](../docs-cache/how-to/how-to-get-started-with-rest-api.md)
  - Swagger URL for REST API · Authentication · Authorize with REST API using Key · Authorize with REST API using ADFS · Location header · Examples
- **Getting started** — [how-to/how-to-get-started-with-zervicepoint-powershell-management/](https://docs.zervicepoint.com/how-to/how-to-get-started-with-zervicepoint-powershell-management/) · [lokal](../docs-cache/how-to/how-to-get-started-with-zervicepoint-powershell-management.md)
  - Introduction to PowerShell Management · Overview · Environment Variables · Authentication and access control · Acquiring and setting a key · Acquiring and setting a security token · What you can do with Zervicepoint PowerShell Management · Examples · CmdLets and syntax
- **Implement isolation** — [how-to/how-to-implement-client-web-service-isolation/](https://docs.zervicepoint.com/how-to/how-to-implement-client-web-service-isolation/) · [lokal](../docs-cache/how-to/how-to-implement-client-web-service-isolation.md)
  - Introduction · Step-by-step guide · Examples
- **Improve performance** — [how-to/how-to-improve-the-performance-of-client-web-service/](https://docs.zervicepoint.com/how-to/how-to-improve-the-performance-of-client-web-service/) · [lokal](../docs-cache/how-to/how-to-improve-the-performance-of-client-web-service.md)
- **Install and configure a plugin** — [how-to/how-to-install-and-configure-a-zervicepoint-plugin/](https://docs.zervicepoint.com/how-to/how-to-install-and-configure-a-zervicepoint-plugin/) · [lokal](../docs-cache/how-to/how-to-install-and-configure-a-zervicepoint-plugin.md)
  - Related content · Information · Configuration
- **Make a copy of a service** — [how-to/how-to-make-a-copy-of-a-service-with-zervicepoint-powershell-management/](https://docs.zervicepoint.com/how-to/how-to-make-a-copy-of-a-service-with-zervicepoint-powershell-management/) · [lokal](../docs-cache/how-to/how-to-make-a-copy-of-a-service-with-zervicepoint-powershell-management.md)
  - Set the ZervicePoint Powershell environment variables (ZPAPIURL, ZPAPIADFSHOST and ZPAPIAUDIENCEURI) if not already set · Import the ZervicePoint Powershell module · Acquire a security token from your ADFS server · Get the service you want to make a copy of, and its associated process · Create a new process with a different name · Create a new service with a new name, displayname and process reference
- **Migration guide** — [how-to/how-to-migrate-to-new-ui/](https://docs.zervicepoint.com/how-to/how-to-migrate-to-new-ui/) · [lokal](../docs-cache/how-to/how-to-migrate-to-new-ui.md)
  - Breaking changes in the New UI and Why we have done these changes · Common direct DOM manipulation/access scenarios · Custom loading indicator · Custom validation · Changing field size · Dynamic text messages (injecting DOM elements) · Line feed, put form field on new row · Dynamically set fields as readonly and disable/enable · Hide/Show form fields · Scrape form for use in email · Disable/Enable submit button · Window load · OnChange · OrderDetailsHTML · Validation for personal number · Dynamic required field
- **Migrate Zervicepoint to new server** — [how-to/how-to-migrate-zervicepoint-to-new-server/](https://docs.zervicepoint.com/how-to/how-to-migrate-zervicepoint-to-new-server/) · [lokal](../docs-cache/how-to/how-to-migrate-zervicepoint-to-new-server.md)
  - Step-by-step guide
- **Place an order** — [how-to/how-to-place-an-order-with-zervicepoint-powershell-management/](https://docs.zervicepoint.com/how-to/how-to-place-an-order-with-zervicepoint-powershell-management/) · [lokal](../docs-cache/how-to/how-to-place-an-order-with-zervicepoint-powershell-management.md)
  - Check out the latest examples for New-ZPOrder · Multi field service · Dynamic drop down service · Service selector service
- **Place order using REST API** — [how-to/how-to-place-order-with-rest-api/](https://docs.zervicepoint.com/how-to/how-to-place-order-with-rest-api/) · [lokal](../docs-cache/how-to/how-to-place-order-with-rest-api.md)
  - Lookup ProfileId for the user · Lookup UniqueId of service · Place order · Place order with fields input
- **Point to new sql instance** — [how-to/how-to-point-zp-to-new-sql-instance/](https://docs.zervicepoint.com/how-to/how-to-point-zp-to-new-sql-instance/) · [lokal](../docs-cache/how-to/how-to-point-zp-to-new-sql-instance.md)
- **Set AdminWeb to port 443** — [how-to/how-to-set-adminweb-to-port-443/](https://docs.zervicepoint.com/how-to/how-to-set-adminweb-to-port-443/) · [lokal](../docs-cache/how-to/how-to-set-adminweb-to-port-443.md)
  - IIS · Webconfig · SQL · Configuring IIS Machine Key · Implementing the Machine Key Configuration · Last Step
- **Setup ProvisioningSystem to authenticate with Key** — [how-to/how-to-setup-provisioningsystem-to-authenticate-with-key/](https://docs.zervicepoint.com/how-to/how-to-setup-provisioningsystem-to-authenticate-with-key/) · [lokal](../docs-cache/how-to/how-to-setup-provisioningsystem-to-authenticate-with-key.md)
  - Instructions
- **Setup key authentication** — [how-to/how-to-setup-zervicepoint-powershell-management-to-work-with-key/](https://docs.zervicepoint.com/how-to/how-to-setup-zervicepoint-powershell-management-to-work-with-key/) · [lokal](../docs-cache/how-to/how-to-setup-zervicepoint-powershell-management-to-work-with-key.md)
  - Instructions
- **How to subscribe to provisioning system events** — [how-to/how-to-subscribe-to-provisioning-system-events/](https://docs.zervicepoint.com/how-to/how-to-subscribe-to-provisioning-system-events/) · [lokal](../docs-cache/how-to/how-to-subscribe-to-provisioning-system-events.md)
  - ServiceRunning event · ServiceRunning arguments · ServiceStopped event · ServiceStopped arguments · InventoryRunning event · InventoryRunning arguments · InventoryCompleted event · InventoryCompleted arguments · ProviderRunning event · ProviderRunning arguments · ProviderCompleted event · ProviderCompleted arguments · Examples
- **Test connection** — [how-to/how-to-test-adfs-connection/](https://docs.zervicepoint.com/how-to/how-to-test-adfs-connection/) · [lokal](../docs-cache/how-to/how-to-test-adfs-connection.md)
- **Upgrade Service Fabric** — [how-to/how-to-upgrade-service-fabric/](https://docs.zervicepoint.com/how-to/how-to-upgrade-service-fabric/) · [lokal](../docs-cache/how-to/how-to-upgrade-service-fabric.md)
  - Overview · Requirements · Media · Upgrade Steps · Step 1 · Step 2 · Step 3 · Step 4 · Step 5 · Step 6 · Step 7 · Step 8 · Step 9 · Step 10 · Step 11 · Step 12 · Step 13 · Step 14 · Step 15 · Step 16
- **Upgrade Service Bus to support TLS 1.2** — [how-to/how-to-upgrade-servicebus-to-support-tls12/](https://docs.zervicepoint.com/how-to/how-to-upgrade-servicebus-to-support-tls12/) · [lokal](../docs-cache/how-to/how-to-upgrade-servicebus-to-support-tls12.md)
  - Overview · Assumptions · Requirements · Stop Services · Remove SB Host · Uninstall ServiceBus 1.1 and Windows Fabric · Install Service Bus with TLS 1.2 · Upgrade Service Bus Farm · Add Service Bus node back to farm · Upgrade Workflow Manager to CU5 · Post-Upgrade steps for Workflow Manager to CU5 · Ensure ServiceBus and Workflow Manager is running · Post-Configuration · Force .NET to use TLS 1.2
- **Use the maintenance web** — [how-to/how-to-use-the-zervicepoint-maintenance-web/](https://docs.zervicepoint.com/how-to/how-to-use-the-zervicepoint-maintenance-web/) · [lokal](../docs-cache/how-to/how-to-use-the-zervicepoint-maintenance-web.md)
  - Scenario 1: Stopping and starting sites · Scenario 2: Using IIS redirection · Method 1: Using HTTP Redirect · Method 2: Using URL Rewrite with a Redirect rule · Scenario 3: Using DNS
- **Working with Activities and Fields Across Zervicepoint Versions** — [how-to/how-to-work-with-copied-service-and-process-json/](https://docs.zervicepoint.com/how-to/how-to-work-with-copied-service-and-process-json/) · [lokal](../docs-cache/how-to/how-to-work-with-copied-service-and-process-json.md)
  - Overview · Copying Between Different Versions · Version Compatibility Warning · Recommended Approach
- **Working with service versions** — [how-to/how-to-work-with-draft/](https://docs.zervicepoint.com/how-to/how-to-work-with-draft/) · [lokal](../docs-cache/how-to/how-to-work-with-draft.md)
  - Creating a draft version · Highlighting of draft in admin web · A sandbox for testing before publishing · Publishing a draft service · Changing versions
- **Write a role main rule** — [how-to/how-to-write-role-main-rule-when-rule-author-doesnt-have-the-claim/](https://docs.zervicepoint.com/how-to/how-to-write-role-main-rule-when-rule-author-doesnt-have-the-claim/) · [lokal](../docs-cache/how-to/how-to-write-role-main-rule-when-rule-author-doesnt-have-the-claim.md)
  - Step-by-step guide
- **Authentication** — [how-to/rest-api-authentication-sample/](https://docs.zervicepoint.com/how-to/rest-api-authentication-sample/) · [lokal](../docs-cache/how-to/rest-api-authentication-sample.md)
  - Retrieve SAML token using Username authentication · Retrieve SAML token using Windows authentication
- **Additional Examples** — [how-to/rest-api-examples/](https://docs.zervicepoint.com/how-to/rest-api-examples/) · [lokal](../docs-cache/how-to/rest-api-examples.md)
  - Get all delegations created by a user · Get all delegations · Get all active delegations · Get all delegations to a delegatee · Upload media
- **Switch from ADFS to Azure AD** — [how-to/switch-from-adfs-to-azure-ad/](https://docs.zervicepoint.com/how-to/switch-from-adfs-to-azure-ad/) · [lokal](../docs-cache/how-to/switch-from-adfs-to-azure-ad.md)
  - How to set ALL user profiles to Temporary:
- **Why you should use the new UI** — [how-to/why-you-should-use-the-new-ui/](https://docs.zervicepoint.com/how-to/why-you-should-use-the-new-ui/) · [lokal](../docs-cache/how-to/why-you-should-use-the-new-ui.md)
  - Specific features only available in the new UI

## Plugins

- **Active Directory Construct File** — [plugins/plugin-active-directory-construct-file/](https://docs.zervicepoint.com/plugins/plugin-active-directory-construct-file/) · [lokal](../docs-cache/plugins/plugin-active-directory-construct-file.md)
  - Example Users and Computers · Elements · Example Groups · Examples PowerShell · Function and Construct Name (activity attributes) · Configuration (activity child element) · Construct (activity child element) · Blacklist · Example blacklisting words
- **Active Directory Plugin** — [plugins/plugin-active-directory/](https://docs.zervicepoint.com/plugins/plugin-active-directory/) · [lokal](../docs-cache/plugins/plugin-active-directory.md)
  - Data Sources · Activities · Installation and Configuration · Update Provider Config · Update dropdown.xml
- **Get started** — [plugins/plugin-assently-get-started/](https://docs.zervicepoint.com/plugins/plugin-assently-get-started/) · [lokal](../docs-cache/plugins/plugin-assently-get-started.md)
  - Sign Agreement · Sign Agreement - Local File · Sign Agreement - JSON · Sign Agreement - JSON + AD Plugin
- **Assently E-Sign Plugin** — [plugins/plugin-assently/](https://docs.zervicepoint.com/plugins/plugin-assently/) · [lokal](../docs-cache/plugins/plugin-assently.md)
  - Activities · Installation and Configuration · Update Provider Config · Dependencies
- **Exchange Plugin** — [plugins/plugin-exchange/](https://docs.zervicepoint.com/plugins/plugin-exchange/) · [lokal](../docs-cache/plugins/plugin-exchange.md)
  - Data Sources · Activities · Installation and Configuration · Update Provider Config · Dependencies
- **Files and Folder Plugin** — [plugins/plugin-files-and-folder/](https://docs.zervicepoint.com/plugins/plugin-files-and-folder/) · [lokal](../docs-cache/plugins/plugin-files-and-folder.md)
  - Data Sources · Activities · Installation and Configuration · Update Provider Config
- **Link Mobility Plugin** — [plugins/plugin-linkmobility/](https://docs.zervicepoint.com/plugins/plugin-linkmobility/) · [lokal](../docs-cache/plugins/plugin-linkmobility.md)
  - Activities · Installation and Configuration · Credential Store · Update Provider Config
- **Microsoft Office 365** — [plugins/plugin-ms-o365/](https://docs.zervicepoint.com/plugins/plugin-ms-o365/) · [lokal](../docs-cache/plugins/plugin-ms-o365.md)
  - Prerequisites · Installation and Configuration · Update Provider Config · Dependencies · License Delegation configuration · License Delegation json example
- **Microsoft Project Online Plugin** — [plugins/plugin-ms-project/](https://docs.zervicepoint.com/plugins/plugin-ms-project/) · [lokal](../docs-cache/plugins/plugin-ms-project.md)
  - Installation and Configuration · Update Provider Config · Dependencies
- **SCCM Package Plugin** — [plugins/plugin-ms-sccm-package/](https://docs.zervicepoint.com/plugins/plugin-ms-sccm-package/) · [lokal](../docs-cache/plugins/plugin-ms-sccm-package.md)
  - Installation and Configuration · Update Provider Config · Dependencies
- **Microsoft SCCM** — [plugins/plugin-ms-sccm/](https://docs.zervicepoint.com/plugins/plugin-ms-sccm/) · [lokal](../docs-cache/plugins/plugin-ms-sccm.md)
  - Installation and Configuraiton · Update Provider Config · Dependencies
- **Microsoft SCSM Plugin** — [plugins/plugin-ms-scsm/](https://docs.zervicepoint.com/plugins/plugin-ms-scsm/) · [lokal](../docs-cache/plugins/plugin-ms-scsm.md)
  - Update Provider Config
- **PDF Automator Plugin** — [plugins/plugin-pdf-automator/](https://docs.zervicepoint.com/plugins/plugin-pdf-automator/) · [lokal](../docs-cache/plugins/plugin-pdf-automator.md)
  - Data Sources · Activities · Installation and Configuration · Update Provider Config
- **Person Lookup(SWE) Plugin** — [plugins/plugin-personlookup-swe/](https://docs.zervicepoint.com/plugins/plugin-personlookup-swe/) · [lokal](../docs-cache/plugins/plugin-personlookup-swe.md)
  - Installation and Configuration · Update Provider Config · Personal numbers to use for test
- **Person Lookup Plugin** — [plugins/plugin-personlookup/](https://docs.zervicepoint.com/plugins/plugin-personlookup/) · [lokal](../docs-cache/plugins/plugin-personlookup.md)
  - Activities · Webservices · Installation and Configuration · Credential Store · Update Provider Config · Dependencies
- **Product Catalog** — [plugins/plugin-productcatalog/](https://docs.zervicepoint.com/plugins/plugin-productcatalog/) · [lokal](../docs-cache/plugins/plugin-productcatalog.md)
  - Installation and Configuration · Update Provider Config
- **Usage** — [plugins/plugin-scrive-usage/](https://docs.zervicepoint.com/plugins/plugin-scrive-usage/) · [lokal](../docs-cache/plugins/plugin-scrive-usage.md)
  - Activities · Get document status · Get document · Start signing process from file · Start signing process from file with json input · Start signing process from template · Start signing process from template with json input · Validations · Uploaded Files · Scrive Templates · Json Input · Partial Document · Parties · Partial Document Example · Full Document · Example Services · Start signing process - Uploaded File · Start signing process - Template · Start signing process - Uploaded File With JSON · Start signing process - Template With JSON · Start signing process - Partial Document · Start signing process - Full Document
- **Scrive Plugin** — [plugins/plugin-scrive/](https://docs.zervicepoint.com/plugins/plugin-scrive/) · [lokal](../docs-cache/plugins/plugin-scrive.md)
  - Activities · Installation and Configuration · Prerequisites · OAuth Token · Credential Store · Update Provider Config · Dependencies
- **ServiceNow** — [plugins/plugin-servicenow/](https://docs.zervicepoint.com/plugins/plugin-servicenow/) · [lokal](../docs-cache/plugins/plugin-servicenow.md)
  - Data Sources · Activities
- **Timezone and Culture** — [plugins/plugin-timezone-and-culture/](https://docs.zervicepoint.com/plugins/plugin-timezone-and-culture/) · [lokal](../docs-cache/plugins/plugin-timezone-and-culture.md)
  - Data Sources
- **Anatomy of a Zervicepoint plugin** — [plugins/plugins/](https://docs.zervicepoint.com/plugins/plugins/) · [lokal](../docs-cache/plugins/plugins.md)
  - PowerShell Plugin · Folder Structure · Configuration · Configure provider config · Configure dropdown.xml · Configure Data sources · Add Credentials/Secrets · Dependencies · Installation Path

## Plugins och malltjänster

- **Template services** — [plugins-and-template-services/template-services/](https://docs.zervicepoint.com/plugins-and-template-services/template-services/) · [lokal](../docs-cache/plugins-and-template-services/template-services.md)
  - How do I install template services? · Prerequisites · Installation · Template services · Active directory · Azure · Collaboration

## Molnonboarding och worker

- **Sign up** — [onboarding/cloud-onboarding-signup/](https://docs.zervicepoint.com/onboarding/cloud-onboarding-signup/) · [lokal](../docs-cache/onboarding/cloud-onboarding-signup.md)
  - Sign up · Authentication · Azure AD · ADFS · ADFS relying party trust · Create ADFS Relying Party Trust using PowerShell · Next steps
- **Install worker** — [onboarding/cloud-onboarding-worker-deployment/](https://docs.zervicepoint.com/onboarding/cloud-onboarding-worker-deployment/) · [lokal](../docs-cache/onboarding/cloud-onboarding-worker-deployment.md)
  - Setup signing certificates for Client Web Service · Download Token Signing Certificate · Generate Data Signing Certificate · Download Zervicepoint media · Install Zervicepoint Worker · Generate Provisioning Key · Add ProvisioningKey to service account credential store · Start Services · Next steps
- **Common worker installation issues** — [onboarding/cloud-onboarding-worker-help/](https://docs.zervicepoint.com/onboarding/cloud-onboarding-worker-help/) · [lokal](../docs-cache/onboarding/cloud-onboarding-worker-help.md)
  - No response from dropdown/webservice · No DNS records exists for Client web service · Name not resolved · Incorrect token/data signing configuraiton · Private Key missing for Data signing certificate / InvalidKey_OrCertificateForSigning · Private Key missing for Data signing certificate · ProvisioningSystem · Incorrect/Missing worker key for ProvisioningSystem
- **Plan for worker installation** — [onboarding/cloud-onboarding-worker-plan/](https://docs.zervicepoint.com/onboarding/cloud-onboarding-worker-plan/) · [lokal](../docs-cache/onboarding/cloud-onboarding-worker-plan.md)
  - List of prerequisites for Zervicepoint Worker · OS requirements · Windows Features requirements · Service Accounts · Service account for Client Web Service · Service account for Provisioning System service · Network · Client web service · DNS record · SSL Certificate · Configure Client Web Service URL · Recommended · Next steps

## Infrastruktur och installation

- **Azure Login** — [infrastructure/azuread-federation/](https://docs.zervicepoint.com/infrastructure/azuread-federation/) · [lokal](../docs-cache/infrastructure/azuread-federation.md)
  - Register Azure Application · Install Microsoft Azure CLI · Login to Azure · Create Azure Application · Add AzureAppSecret to Application Pool service account · Adding claims to an Azure Application (optional) · Add claims using powershell eample
- **Cloud Onboarding** — [infrastructure/cloud-onboarding/](https://docs.zervicepoint.com/infrastructure/cloud-onboarding/) · [lokal](../docs-cache/infrastructure/cloud-onboarding.md)
  - Sign-up process · Store URL · Authentication · AD FS · Azure AD · I want to integrate with my on-premise environment · List of Prerequisits for Zervicepoint Cloud Server · Client web service
- **Setup Microsoft ServiceBus / Workflow Manager** — [infrastructure/installer-workflowmanager/](https://docs.zervicepoint.com/infrastructure/installer-workflowmanager/) · [lokal](../docs-cache/infrastructure/installer-workflowmanager.md)
  - High-Level steps for installing Service Bus / Workflow Manager · Before you begin · Create Service Account · Create Admin Group (Optional) · Download Service Bus / Workflow Manager · Install Service Bus / Workflow Manager binaries · Step 1 · Step 2 · Step 3 · Step 4 · Step 5 · Step 6 · Step 7 · Workflow Manager Configuration Wizard · Select SQL Server Instance · Enter Service Account details / Generate certificate · Configure Admin Group · Service Bus Configuration · Select SQL Server Instance · Enter Service Account details / Generate certificate · Configure Admin Group · Summary · Create Namespace for zervicepoint · Force .NET to use TLS 1.2 · Common issues / Troubleshooting
- **Zervicepoint Installer** — [infrastructure/installer/](https://docs.zervicepoint.com/infrastructure/installer/) · [lokal](../docs-cache/infrastructure/installer.md)
  - Installation · Select Features · Database Settings · Authentication Settings · Web Site Settings · Process System Settings · Provisioning and API Settings · PowerShell Module Settings · Eventlog Settings · Installation Log
- **Network Diagram** — [infrastructure/network-diagram/](https://docs.zervicepoint.com/infrastructure/network-diagram/) · [lokal](../docs-cache/infrastructure/network-diagram.md)
  - Components · Single Server instance Setup · Multi-Tenant (No HA) Setup · Multi-Tenant (HA 1) Setup · Multi-Tenant (HA 2) Setup
- **Overview** — [infrastructure/overview/](https://docs.zervicepoint.com/infrastructure/overview/) · [lokal](../docs-cache/infrastructure/overview.md)
  - Components · Zervicepoint topologies · On premise - Single Server setup · On premise - Multi-Server setup · Multi-Tenant Setup · Service Accounts
- **Pre-Installation checklist** — [infrastructure/pre-install-checklist/](https://docs.zervicepoint.com/infrastructure/pre-install-checklist/) · [lokal](../docs-cache/infrastructure/pre-install-checklist.md)
- **Requirements** — [infrastructure/requirements/](https://docs.zervicepoint.com/infrastructure/requirements/) · [lokal](../docs-cache/infrastructure/requirements.md)
  - Operating System · SQL Server · Minimum Hardware Requirements · Software Requirements · Supported languages: · Authentication
- **Single Server Setup - Single Store** — [infrastructure/single-server-setup/](https://docs.zervicepoint.com/infrastructure/single-server-setup/) · [lokal](../docs-cache/infrastructure/single-server-setup.md)
  - Requirements · DNS · Certificate · Service Accounts · Frontend Account · Frontend account permissions · Backend Account · Backend account permissions · Workflow Manager Account · Workflow Manager account permissions · Create Service Accounts · Service Account Permissions · Install Windows Features · Authentication · AzureAD · ADFS · Start ZervicePointSetup · Download zervicepoint media · Features · Database · Authentication Settings · Web site settings · process system · Provisioning and API · Powershell module · Post-Configuration · Verify permissions · Restart ServiceBus and Workflow Manager · Add AzureAppSecret to frontend account · Login to zervicepoint · Configure ProvisioningSystem service · Update ClientWebService config with generated certificate thumbprint · Start Zervicepoint Process System · Create test service

## ZerFlow (arbetsflödesmotor)

- **Configuring Zervicepoint for engine selection** — [zerflow/Engine-selection/](https://docs.zervicepoint.com/zerflow/Engine-selection/) · [lokal](../docs-cache/zerflow/Engine-selection.md)
  - Zervicepoint configuration files
- **ZerFlow install guide** — [zerflow/ZerFlow-install-guide/](https://docs.zervicepoint.com/zerflow/ZerFlow-install-guide/) · [lokal](../docs-cache/zerflow/ZerFlow-install-guide.md)
  - Prerequisites · **Zervicepoint version 1.35 or later** · **.NET 10.0.3 Desktop Runtime or later** · **Internet access** · **SQL Server** · Zerflow Installer · **1. Start the installer** · **2. Service Account Settings** · **3. Database Settings** · **4. Zerflow API Settings** · **5. Zerflow Queue Settings** · **6. Zerflow Engine Settings** · **7. License & Version Settings** · **Buttons**
- **ZerFlow introduction** — [zerflow/ZerFlow-introduction/](https://docs.zervicepoint.com/zerflow/ZerFlow-introduction/) · [lokal](../docs-cache/zerflow/ZerFlow-introduction.md)
  - Some key features:
- **Breaking changes** — [zerflow/breaking-changes/](https://docs.zervicepoint.com/zerflow/breaking-changes/) · [lokal](../docs-cache/zerflow/breaking-changes.md)
  - Background
- **Zerflow Engine Manager** — [zerflow/engine-manager/](https://docs.zervicepoint.com/zerflow/engine-manager/) · [lokal](../docs-cache/zerflow/engine-manager.md)
  - **Refresh icon** · **Add** · **Remove** · **Start All** · **Stop All**
- **Coming soon** — [zerflow/release-notes/coming-soon/](https://docs.zervicepoint.com/zerflow/release-notes/coming-soon/) · [lokal](../docs-cache/zerflow/release-notes/coming-soon.md)

## Felsökning

- **A specific service stays in Queued** — [troubleshooting/a-specific-service-stays-in-queued/](https://docs.zervicepoint.com/troubleshooting/a-specific-service-stays-in-queued/) · [lokal](../docs-cache/troubleshooting/a-specific-service-stays-in-queued.md)
  - Problem · Solution · Related articles
- **After upgrading to 1.12.1367 on a tenant you get error "an unsecured or incorrectly secured fault was received"** — [troubleshooting/after-upgrading-to-1-12-1367-on-a-tenant-you-get-error-an-unsecured-or-incorrectly-secured-fault-was-received/](https://docs.zervicepoint.com/troubleshooting/after-upgrading-to-1-12-1367-on-a-tenant-you-get-error-an-unsecured-or-incorrectly-secured-fault-was-received/) · [lokal](../docs-cache/troubleshooting/after-upgrading-to-1-12-1367-on-a-tenant-you-get-error-an-unsecured-or-incorrectly-secured-fault-was-received.md)
  - Problem · Solution · On Frontend Servers · On Tenant where error occurs
- **After upgrading to 1.7.913, services or shared processes with manual tasks get stuck in Queued** — [troubleshooting/after-upgrading-to-1-7-913-services-or-shared-processes-with-manual-tasks-get-stuck-in-queued/](https://docs.zervicepoint.com/troubleshooting/after-upgrading-to-1-7-913-services-or-shared-processes-with-manual-tasks-get-stuck-in-queued/) · [lokal](../docs-cache/troubleshooting/after-upgrading-to-1-7-913-services-or-shared-processes-with-manual-tasks-get-stuck-in-queued.md)
  - Problem · Solution · Option 1: Open and save · Option 2: Run SQL fix
- **An item with the same key has already been added** — [troubleshooting/an-item-with-the-same-key-has-already-been-added/](https://docs.zervicepoint.com/troubleshooting/an-item-with-the-same-key-has-already-been-added/) · [lokal](../docs-cache/troubleshooting/an-item-with-the-same-key-has-already-been-added.md)
  - Problem · Solution · Related articles
- **Authentication exception when using an NLB solution with Workflow Manager** — [troubleshooting/authentication-exception-when-using-an-nlb-solution-with-workflow-manager/](https://docs.zervicepoint.com/troubleshooting/authentication-exception-when-using-an-nlb-solution-with-workflow-manager/) · [lokal](../docs-cache/troubleshooting/authentication-exception-when-using-an-nlb-solution-with-workflow-manager.md)
  - Problem · Solution · Related articles
- **Bad Request exception from Zervicepoint Powershell Management commands** — [troubleshooting/bad-request-exception-from-zppsmgmt-commands/](https://docs.zervicepoint.com/troubleshooting/bad-request-exception-from-zppsmgmt-commands/) · [lokal](../docs-cache/troubleshooting/bad-request-exception-from-zppsmgmt-commands.md)
  - Problem · Cause · Solution
- **Cannot create unknown type** — [troubleshooting/cannot-create-unknown-type/](https://docs.zervicepoint.com/troubleshooting/cannot-create-unknown-type/) · [lokal](../docs-cache/troubleshooting/cannot-create-unknown-type.md)
  - Problem · Solution · The following files should exist in this folder:
- **Can't generate Token signing certificate** — [troubleshooting/cant-generate-token-signing-certificate/](https://docs.zervicepoint.com/troubleshooting/cant-generate-token-signing-certificate/) · [lokal](../docs-cache/troubleshooting/cant-generate-token-signing-certificate.md)
  - Problem · Solution · Related articles
- **Client Web Service calls gets aborted** — [troubleshooting/client-web-service-calls-gets-aborted/](https://docs.zervicepoint.com/troubleshooting/client-web-service-calls-gets-aborted/) · [lokal](../docs-cache/troubleshooting/client-web-service-calls-gets-aborted.md)
  - Problem · Solution
- **Client Web Service Error: Cannot access a closed file** — [troubleshooting/client-web-service-error-cannot-access-a-closed-file/](https://docs.zervicepoint.com/troubleshooting/client-web-service-error-cannot-access-a-closed-file/) · [lokal](../docs-cache/troubleshooting/client-web-service-error-cannot-access-a-closed-file.md)
  - Problem · Solution
- **Client web service is not configured or certificates have expired** — [troubleshooting/client-web-service-is-not-configured-or-certificates-have-expired/](https://docs.zervicepoint.com/troubleshooting/client-web-service-is-not-configured-or-certificates-have-expired/) · [lokal](../docs-cache/troubleshooting/client-web-service-is-not-configured-or-certificates-have-expired.md)
  - Problem · Solution
- **Client Web Service stops responding** — [troubleshooting/client-web-service-stops-responding/](https://docs.zervicepoint.com/troubleshooting/client-web-service-stops-responding/) · [lokal](../docs-cache/troubleshooting/client-web-service-stops-responding.md)
  - Problem · Solution · Related articles
- **Common AD FS problems for ProvisioningSystem after installation** — [troubleshooting/common-ad-fs-problems-for-provisioningsystem-after-installation/](https://docs.zervicepoint.com/troubleshooting/common-ad-fs-problems-for-provisioningsystem-after-installation/) · [lokal](../docs-cache/troubleshooting/common-ad-fs-problems-for-provisioningsystem-after-installation.md)
  - Checklist · If SPN is not correctly configured · If the hostname for ADFS website · If the ADFS-server doesn't respond · If the wrong identity is specified · If the audience uri is incorrect
- **Could not get next job: System.ServiceModel.EndpointNotFoundException** — [troubleshooting/could-not-get-next-job/](https://docs.zervicepoint.com/troubleshooting/could-not-get-next-job/) · [lokal](../docs-cache/troubleshooting/could-not-get-next-job.md)
  - Problem · Solution
- **Datetime objects not working correctly** — [troubleshooting/datetime-objects-not-working-correctly/](https://docs.zervicepoint.com/troubleshooting/datetime-objects-not-working-correctly/) · [lokal](../docs-cache/troubleshooting/datetime-objects-not-working-correctly.md)
  - Problem · Solution
- **.NET 4.6 might cause unpatched Service Bus 1.1 for Windows server to become unresponsive** — [troubleshooting/dotNet-4-6-might-cause-unpatched-service-bus-1-1-for-windows-server-to-become-unresposive/](https://docs.zervicepoint.com/troubleshooting/dotNet-4-6-might-cause-unpatched-service-bus-1-1-for-windows-server-to-become-unresposive/) · [lokal](../docs-cache/troubleshooting/dotNet-4-6-might-cause-unpatched-service-bus-1-1-for-windows-server-to-become-unresposive.md)
  - Problem · Solution
- **Empty id results in dynamic drop down causes object reference error** — [troubleshooting/empty-results-in-dynamic-drop-down-causes-object-reference-error/](https://docs.zervicepoint.com/troubleshooting/empty-results-in-dynamic-drop-down-causes-object-reference-error/) · [lokal](../docs-cache/troubleshooting/empty-results-in-dynamic-drop-down-causes-object-reference-error.md)
  - Problem · Solution
- **Error 403.14** — [troubleshooting/error-403-14/](https://docs.zervicepoint.com/troubleshooting/error-403-14/) · [lokal](../docs-cache/troubleshooting/error-403-14.md)
  - Problem · Solution
- **Error when enabling Lync/Skype for Business user (Enable-ZPS4BUser)** — [troubleshooting/error-when-enabling-lync-skype-for-business-user/](https://docs.zervicepoint.com/troubleshooting/error-when-enabling-lync-skype-for-business-user/) · [lokal](../docs-cache/troubleshooting/error-when-enabling-lync-skype-for-business-user.md)
  - Problem · Solution
- **Failed to authenticate session** — [troubleshooting/failed-to-authenticate-session/](https://docs.zervicepoint.com/troubleshooting/failed-to-authenticate-session/) · [lokal](../docs-cache/troubleshooting/failed-to-authenticate-session.md)
  - Problem · Solution · If you have a load balanced frontend (two or more servers) · Related articles
- **Import-PSSession causes memory leak in Provisioning System** — [troubleshooting/import-pssession-causes-memory-leak-in-provisioning-system/](https://docs.zervicepoint.com/troubleshooting/import-pssession-causes-memory-leak-in-provisioning-system/) · [lokal](../docs-cache/troubleshooting/import-pssession-causes-memory-leak-in-provisioning-system.md)
  - Problem · Solution
- **Installation fails with error code 1603** — [troubleshooting/installation-fails-with-error-code-1603/](https://docs.zervicepoint.com/troubleshooting/installation-fails-with-error-code-1603/) · [lokal](../docs-cache/troubleshooting/installation-fails-with-error-code-1603.md)
  - Problem · Solution
- **Installing .NET Framework 4.6 causes ZervicePoint versions prior to 1.7.871 to stop working** — [troubleshooting/installing-net-framework-4-6-causes-zervicepoint-versions-prior-to-1-7-871-to-stop-working/](https://docs.zervicepoint.com/troubleshooting/installing-net-framework-4-6-causes-zervicepoint-versions-prior-to-1-7-871-to-stop-working/) · [lokal](../docs-cache/troubleshooting/installing-net-framework-4-6-causes-zervicepoint-versions-prior-to-1-7-871-to-stop-working.md)
- **Installing Skype for Business Server 2015 Core Components causes ZervicePoint to stop working** — [troubleshooting/installing-skype-for-business-server-2015-core-components-causes-zervicepoint-to-stop-working/](https://docs.zervicepoint.com/troubleshooting/installing-skype-for-business-server-2015-core-components-causes-zervicepoint-to-stop-working/) · [lokal](../docs-cache/troubleshooting/installing-skype-for-business-server-2015-core-components-causes-zervicepoint-to-stop-working.md)
  - Problem · Solution
- **Missing Managed User in Service Bus ZervicePoint Namespace** — [troubleshooting/missing-managed-user-in-zervicepoint-namespace/](https://docs.zervicepoint.com/troubleshooting/missing-managed-user-in-zervicepoint-namespace/) · [lokal](../docs-cache/troubleshooting/missing-managed-user-in-zervicepoint-namespace.md)
  - Problem · Solution
- **No domain in Provisioning account** — [troubleshooting/no-domain-in-provisioning-account/](https://docs.zervicepoint.com/troubleshooting/no-domain-in-provisioning-account/) · [lokal](../docs-cache/troubleshooting/no-domain-in-provisioning-account.md)
  - Problem · Solution
- **ObjectNotFound exception from long running ZervicePoint PowerShell Management commands** — [troubleshooting/objectnotfound-exception-from-long-running-zervicepoint-powershell-management-commands/](https://docs.zervicepoint.com/troubleshooting/objectnotfound-exception-from-long-running-zervicepoint-powershell-management-commands/) · [lokal](../docs-cache/troubleshooting/objectnotfound-exception-from-long-running-zervicepoint-powershell-management-commands.md)
  - Problem · Cause · Method 1 · Method 2 · Solution
- **Orders are not in numerical order** — [troubleshooting/orders-are-not-in-numerical-order/](https://docs.zervicepoint.com/troubleshooting/orders-are-not-in-numerical-order/) · [lokal](../docs-cache/troubleshooting/orders-are-not-in-numerical-order.md)
  - Problem · Solution · Related articles
- **Orders are not processed and are stuck in Queued state** — [troubleshooting/orders-are-not-processed-and-are-stuck-in-queued-state/](https://docs.zervicepoint.com/troubleshooting/orders-are-not-processed-and-are-stuck-in-queued-state/) · [lokal](../docs-cache/troubleshooting/orders-are-not-processed-and-are-stuck-in-queued-state.md)
  - Problem · Solution · Related articles
- **Orders stuck in process when calling providers after upgrade** — [troubleshooting/orders-stuck-in-process-when-calling-providers-after-upgrade/](https://docs.zervicepoint.com/troubleshooting/orders-stuck-in-process-when-calling-providers-after-upgrade/) · [lokal](../docs-cache/troubleshooting/orders-stuck-in-process-when-calling-providers-after-upgrade.md)
  - Problem · Solution · Related articles
- **Orders stuck in Queued state or Distributed Transaction Manager (MSDTC) errors in the Event Viewer** — [troubleshooting/orders-stuck-in-queued-state-or-distributed-transaction-manager-msdtc-errors-in-the-event-viewer/](https://docs.zervicepoint.com/troubleshooting/orders-stuck-in-queued-state-or-distributed-transaction-manager-msdtc-errors-in-the-event-viewer/) · [lokal](../docs-cache/troubleshooting/orders-stuck-in-queued-state-or-distributed-transaction-manager-msdtc-errors-in-the-event-viewer.md)
  - Problem · Solution · Related articles
- **Provider with multiple additional parameters start but don't complete and duplicate key error in Event log** — [troubleshooting/provider-with-multiple-additional-parameters-start-but-don-t-complete/](https://docs.zervicepoint.com/troubleshooting/provider-with-multiple-additional-parameters-start-but-don-t-complete/) · [lokal](../docs-cache/troubleshooting/provider-with-multiple-additional-parameters-start-but-don-t-complete.md)
  - Problem · Solution · Related articles
- **Provisioning job fails but repeats every hour** — [troubleshooting/provisioning-job-fails-but-repeats-every-hour/](https://docs.zervicepoint.com/troubleshooting/provisioning-job-fails-but-repeats-every-hour/) · [lokal](../docs-cache/troubleshooting/provisioning-job-fails-but-repeats-every-hour.md)
  - Problem · Solution
- **Provisioning system service error in log after upgrade** — [troubleshooting/provisioning-system-service-error-after-upgrade/](https://docs.zervicepoint.com/troubleshooting/provisioning-system-service-error-after-upgrade/) · [lokal](../docs-cache/troubleshooting/provisioning-system-service-error-after-upgrade.md)
  - Problem · Solution · Related articles
- **Error 1923 - ProvisioningSystem could not be installed** — [troubleshooting/provisioningsystem-could-not-be-installed/](https://docs.zervicepoint.com/troubleshooting/provisioningsystem-could-not-be-installed/) · [lokal](../docs-cache/troubleshooting/provisioningsystem-could-not-be-installed.md)
  - Problem · Solution
- **Service Bus error in instances table in WFInstanceManagementDB** — [troubleshooting/service-bus-error-in-instances-table-in-wfinstancemanagementdb/](https://docs.zervicepoint.com/troubleshooting/service-bus-error-in-instances-table-in-wfinstancemanagementdb/) · [lokal](../docs-cache/troubleshooting/service-bus-error-in-instances-table-in-wfinstancemanagementdb.md)
  - Problem · Solution
- **Servicebus stuck in status "starting"** — [troubleshooting/service-bus-stuck-in-status-starting/](https://docs.zervicepoint.com/troubleshooting/service-bus-stuck-in-status-starting/) · [lokal](../docs-cache/troubleshooting/service-bus-stuck-in-status-starting.md)
  - Problem · Solution · Related articles
- **Service Bus transaction log grows ginormous** — [troubleshooting/service-bus-transaction-log-grows-ginormous/](https://docs.zervicepoint.com/troubleshooting/service-bus-transaction-log-grows-ginormous/) · [lokal](../docs-cache/troubleshooting/service-bus-transaction-log-grows-ginormous.md)
  - Problem · Solution · More in this thread
- **System.ArgumentException: An item with the same key has already been added** — [troubleshooting/system-argumentexception-an-item-with-the-same-key-has-already-been-added/](https://docs.zervicepoint.com/troubleshooting/system-argumentexception-an-item-with-the-same-key-has-already-been-added/) · [lokal](../docs-cache/troubleshooting/system-argumentexception-an-item-with-the-same-key-has-already-been-added.md)
  - Problem · Solution · Related articles
- **The remote server returned an error: (400) Bad Request** — [troubleshooting/the-remote-server-returned-an-error-400-bad-request/](https://docs.zervicepoint.com/troubleshooting/the-remote-server-returned-an-error-400-bad-request/) · [lokal](../docs-cache/troubleshooting/the-remote-server-returned-an-error-400-bad-request.md)
  - Problem · Solution
- **There was no endpoint listening at** — [troubleshooting/there-was-no-endpoint-listening/](https://docs.zervicepoint.com/troubleshooting/there-was-no-endpoint-listening/) · [lokal](../docs-cache/troubleshooting/there-was-no-endpoint-listening.md)
  - Problem · Solution · Related articles
- **Timeout exception when using Get-ZPService in ZervicePoint PowerShell Management** — [troubleshooting/timeout-exception-when-using-get-zpservice-in-zervicepoint-powershell-management/](https://docs.zervicepoint.com/troubleshooting/timeout-exception-when-using-get-zpservice-in-zervicepoint-powershell-management/) · [lokal](../docs-cache/troubleshooting/timeout-exception-when-using-get-zpservice-in-zervicepoint-powershell-management.md)
  - Problem · Solution
- **Troubleshooting guidelines** — [troubleshooting/troubleshooting-guidelines/](https://docs.zervicepoint.com/troubleshooting/troubleshooting-guidelines/) · [lokal](../docs-cache/troubleshooting/troubleshooting-guidelines.md)
  - Problem · Solution · System-related issues · Order-related issues
- **Unable to login to ZervicePoint (version prior to 1.7.871) after installing .Net Framework 4.6** — [troubleshooting/unable-to-login-to-zervicepoint-version-prior-to-1-7-871-after-installing-net-framework-4-6/](https://docs.zervicepoint.com/troubleshooting/unable-to-login-to-zervicepoint-version-prior-to-1-7-871-after-installing-net-framework-4-6/) · [lokal](../docs-cache/troubleshooting/unable-to-login-to-zervicepoint-version-prior-to-1-7-871-after-installing-net-framework-4-6.md)
  - Problem · Solution
- **Error Unauthorized when trying to use ZervicePoint PowerShell Management** — [troubleshooting/unauthorized-when-trying-to-use-zervicepoint-powershell-management/](https://docs.zervicepoint.com/troubleshooting/unauthorized-when-trying-to-use-zervicepoint-powershell-management/) · [lokal](../docs-cache/troubleshooting/unauthorized-when-trying-to-use-zervicepoint-powershell-management.md)
  - Problem · Solution · Related articles
- **Use retry functionality when working with PowerShell cmdlets that are not thread safe** — [troubleshooting/use-retry-functionality-when-working-with-powershell-cmdlets-that-are-not-thread-safe/](https://docs.zervicepoint.com/troubleshooting/use-retry-functionality-when-working-with-powershell-cmdlets-that-are-not-thread-safe/) · [lokal](../docs-cache/troubleshooting/use-retry-functionality-when-working-with-powershell-cmdlets-that-are-not-thread-safe.md)
  - Problem · Solution
- **Using static methods in Powershell 5 classes in modules used by ZervicePoint can cause issues** — [troubleshooting/using-static-methods-in-powershell-classes-in-modules-used-by-zervicepoint-can-cause-issues/](https://docs.zervicepoint.com/troubleshooting/using-static-methods-in-powershell-classes-in-modules-used-by-zervicepoint-can-cause-issues/) · [lokal](../docs-cache/troubleshooting/using-static-methods-in-powershell-classes-in-modules-used-by-zervicepoint-can-cause-issues.md)
  - Problem · Solution
- **WFUtil for cleaning inactive workflows** — [troubleshooting/wfutil-for-cleaning-inactive-workflows/](https://docs.zervicepoint.com/troubleshooting/wfutil-for-cleaning-inactive-workflows/) · [lokal](../docs-cache/troubleshooting/wfutil-for-cleaning-inactive-workflows.md)
  - Problem · Solution · Additional Info
- **Why certain PowerShell Snapins do not load properly in Drop Downs and WebServices** — [troubleshooting/why-certain-powershell-snapins-do-not-load-properly-in-drop-downs-and-webservices/](https://docs.zervicepoint.com/troubleshooting/why-certain-powershell-snapins-do-not-load-properly-in-drop-downs-and-webservices/) · [lokal](../docs-cache/troubleshooting/why-certain-powershell-snapins-do-not-load-properly-in-drop-downs-and-webservices.md)
  - Problem · Solution
- **Workflow manager not trusting root certificate** — [troubleshooting/workflow-manager-not-trusting-root-certificate/](https://docs.zervicepoint.com/troubleshooting/workflow-manager-not-trusting-root-certificate/) · [lokal](../docs-cache/troubleshooting/workflow-manager-not-trusting-root-certificate.md)
  - Problem · Solution
- **Workflow stops with custom Provider activity in started state** — [troubleshooting/workflow-stops-with-custom-provider-activity-in-started-state/](https://docs.zervicepoint.com/troubleshooting/workflow-stops-with-custom-provider-activity-in-started-state/) · [lokal](../docs-cache/troubleshooting/workflow-stops-with-custom-provider-activity-in-started-state.md)
  - Problem · Solution
- **Workflow validation failed with large workflows** — [troubleshooting/workflow-validation-fail-with-large-workflows/](https://docs.zervicepoint.com/troubleshooting/workflow-validation-fail-with-large-workflows/) · [lokal](../docs-cache/troubleshooting/workflow-validation-fail-with-large-workflows.md)
  - Problem · Solution · Related articles
- **Workflow validation failed when using conditional sequence** — [troubleshooting/workflow-validation-failed-when-using-conditional-sequence/](https://docs.zervicepoint.com/troubleshooting/workflow-validation-failed-when-using-conditional-sequence/) · [lokal](../docs-cache/troubleshooting/workflow-validation-failed-when-using-conditional-sequence.md)
  - Problem · Solution · Related articles
- **Workflow validation failed with large workflows** — [troubleshooting/workflow-validation-failed-with-large-workflows/](https://docs.zervicepoint.com/troubleshooting/workflow-validation-failed-with-large-workflows/) · [lokal](../docs-cache/troubleshooting/workflow-validation-failed-with-large-workflows.md)
  - Problem · Solution · Related articles
- **ZervicePoint event log errors and warnings with unique event ids** — [troubleshooting/zervicepoint-unique-event-ids/](https://docs.zervicepoint.com/troubleshooting/zervicepoint-unique-event-ids/) · [lokal](../docs-cache/troubleshooting/zervicepoint-unique-event-ids.md)
  - Description · Events · Userweb Events · Related articles

## Release notes

- **1.35.2** — [release-notes/1.35.2/](https://docs.zervicepoint.com/release-notes/1.35.2/) · [lokal](../docs-cache/release-notes/1.35.2.md)
  - New · Improvement · Fixes
- **1.35.3** — [release-notes/1.35.3/](https://docs.zervicepoint.com/release-notes/1.35.3/) · [lokal](../docs-cache/release-notes/1.35.3.md)
  - Fixes
- **1.20.2076** — [release-notes/Archive/1.20.2076/](https://docs.zervicepoint.com/release-notes/Archive/1.20.2076/) · [lokal](../docs-cache/release-notes/Archive/1.20.2076.md)
  - New features · Issues corrected · New translations · System requirements and Documentation · Providing feedback · Known Issues
- **1.20.2046** — [release-notes/Archive/1.20/](https://docs.zervicepoint.com/release-notes/Archive/1.20/) · [lokal](../docs-cache/release-notes/Archive/1.20.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.21.2116** — [release-notes/Archive/1.21.2116/](https://docs.zervicepoint.com/release-notes/Archive/1.21.2116/) · [lokal](../docs-cache/release-notes/Archive/1.21.2116.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.21.2135** — [release-notes/Archive/1.21.2135/](https://docs.zervicepoint.com/release-notes/Archive/1.21.2135/) · [lokal](../docs-cache/release-notes/Archive/1.21.2135.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.21.2160** — [release-notes/Archive/1.21.2160/](https://docs.zervicepoint.com/release-notes/Archive/1.21.2160/) · [lokal](../docs-cache/release-notes/Archive/1.21.2160.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.21.2184** — [release-notes/Archive/1.21.2184/](https://docs.zervicepoint.com/release-notes/Archive/1.21.2184/) · [lokal](../docs-cache/release-notes/Archive/1.21.2184.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.21.2193** — [release-notes/Archive/1.21.2193/](https://docs.zervicepoint.com/release-notes/Archive/1.21.2193/) · [lokal](../docs-cache/release-notes/Archive/1.21.2193.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.22.2227** — [release-notes/Archive/1.22.2227/](https://docs.zervicepoint.com/release-notes/Archive/1.22.2227/) · [lokal](../docs-cache/release-notes/Archive/1.22.2227.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.22.2284** — [release-notes/Archive/1.22.2284/](https://docs.zervicepoint.com/release-notes/Archive/1.22.2284/) · [lokal](../docs-cache/release-notes/Archive/1.22.2284.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.23.2307** — [release-notes/Archive/1.23.2307/](https://docs.zervicepoint.com/release-notes/Archive/1.23.2307/) · [lokal](../docs-cache/release-notes/Archive/1.23.2307.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.23.2320** — [release-notes/Archive/1.23.2320/](https://docs.zervicepoint.com/release-notes/Archive/1.23.2320/) · [lokal](../docs-cache/release-notes/Archive/1.23.2320.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.23.2345** — [release-notes/Archive/1.23.2345/](https://docs.zervicepoint.com/release-notes/Archive/1.23.2345/) · [lokal](../docs-cache/release-notes/Archive/1.23.2345.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.23.2367** — [release-notes/Archive/1.23.2367/](https://docs.zervicepoint.com/release-notes/Archive/1.23.2367/) · [lokal](../docs-cache/release-notes/Archive/1.23.2367.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.24.2384** — [release-notes/Archive/1.24.2384/](https://docs.zervicepoint.com/release-notes/Archive/1.24.2384/) · [lokal](../docs-cache/release-notes/Archive/1.24.2384.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.24.2410** — [release-notes/Archive/1.24.2410/](https://docs.zervicepoint.com/release-notes/Archive/1.24.2410/) · [lokal](../docs-cache/release-notes/Archive/1.24.2410.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.24.2446** — [release-notes/Archive/1.24.2446/](https://docs.zervicepoint.com/release-notes/Archive/1.24.2446/) · [lokal](../docs-cache/release-notes/Archive/1.24.2446.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.24.2466** — [release-notes/Archive/1.24.2466/](https://docs.zervicepoint.com/release-notes/Archive/1.24.2466/) · [lokal](../docs-cache/release-notes/Archive/1.24.2466.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.25.2487** — [release-notes/Archive/1.25.2487/](https://docs.zervicepoint.com/release-notes/Archive/1.25.2487/) · [lokal](../docs-cache/release-notes/Archive/1.25.2487.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.25.2507** — [release-notes/Archive/1.25.2507/](https://docs.zervicepoint.com/release-notes/Archive/1.25.2507/) · [lokal](../docs-cache/release-notes/Archive/1.25.2507.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.25.2549** — [release-notes/Archive/1.25.2549/](https://docs.zervicepoint.com/release-notes/Archive/1.25.2549/) · [lokal](../docs-cache/release-notes/Archive/1.25.2549.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.26.2592** — [release-notes/Archive/1.26.2592/](https://docs.zervicepoint.com/release-notes/Archive/1.26.2592/) · [lokal](../docs-cache/release-notes/Archive/1.26.2592.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.26.2598** — [release-notes/Archive/1.26.2598/](https://docs.zervicepoint.com/release-notes/Archive/1.26.2598/) · [lokal](../docs-cache/release-notes/Archive/1.26.2598.md)
  - New features · Issues corrected · System requirements and Documentation · Providing feedback · Known Issues
- **1.26.2664** — [release-notes/Archive/1.26.2664/](https://docs.zervicepoint.com/release-notes/Archive/1.26.2664/) · [lokal](../docs-cache/release-notes/Archive/1.26.2664.md)
  - New features and changes · Issues corrected · Known Issues
- **1.26.2677** — [release-notes/Archive/1.26.2677/](https://docs.zervicepoint.com/release-notes/Archive/1.26.2677/) · [lokal](../docs-cache/release-notes/Archive/1.26.2677.md)
  - Issues corrected · Known Issues
- **1.27.2732** — [release-notes/Archive/1.27.2732/](https://docs.zervicepoint.com/release-notes/Archive/1.27.2732/) · [lokal](../docs-cache/release-notes/Archive/1.27.2732.md)
  - New features and changes · Issues corrected · Known Issues
- **1.27.2739** — [release-notes/Archive/1.27.2739/](https://docs.zervicepoint.com/release-notes/Archive/1.27.2739/) · [lokal](../docs-cache/release-notes/Archive/1.27.2739.md)
  - Issues corrected · Known Issues
- **1.27.2753** — [release-notes/Archive/1.27.2753/](https://docs.zervicepoint.com/release-notes/Archive/1.27.2753/) · [lokal](../docs-cache/release-notes/Archive/1.27.2753.md)
  - Issues corrected · Known Issues
- **1.28.2801** — [release-notes/Archive/1.28.2801/](https://docs.zervicepoint.com/release-notes/Archive/1.28.2801/) · [lokal](../docs-cache/release-notes/Archive/1.28.2801.md)
  - New features and changes · Issues corrected · Known Issues
- **1.29.2822** — [release-notes/Archive/1.29.2822/](https://docs.zervicepoint.com/release-notes/Archive/1.29.2822/) · [lokal](../docs-cache/release-notes/Archive/1.29.2822.md)
  - New features and changes · Issues corrected · Known Issues
- **1.29.2851** — [release-notes/Archive/1.29.2851/](https://docs.zervicepoint.com/release-notes/Archive/1.29.2851/) · [lokal](../docs-cache/release-notes/Archive/1.29.2851.md)
  - New features and changes · REST-API update · Visual design updates in the user web · Support for SQL Server 2019 · Issues corrected · Known Issues
- **1.29.2879** — [release-notes/Archive/1.29.2879/](https://docs.zervicepoint.com/release-notes/Archive/1.29.2879/) · [lokal](../docs-cache/release-notes/Archive/1.29.2879.md)
  - Issues corrected · Known Issues
- **1.29.2914** — [release-notes/Archive/1.29.2914/](https://docs.zervicepoint.com/release-notes/Archive/1.29.2914/) · [lokal](../docs-cache/release-notes/Archive/1.29.2914.md)
  - Issues corrected · Known Issues
- **1.30.2958** — [release-notes/Archive/1.30.2958/](https://docs.zervicepoint.com/release-notes/Archive/1.30.2958/) · [lokal](../docs-cache/release-notes/Archive/1.30.2958.md)
  - New features and changes · Max file size setting on file upload field · Max file upload size setting per store · Temporarily disable activities and fields · Link to shared process in Update Service dialog · isValid() - new Z-api function · visible() - Z-api function available on selector object · Changes in the Zervicepoint Powershell module · Issues corrected · Known Issues
- **1.30.3033** — [release-notes/Archive/1.30.3033/](https://docs.zervicepoint.com/release-notes/Archive/1.30.3033/) · [lokal](../docs-cache/release-notes/Archive/1.30.3033.md)
  - Issues corrected · Known Issues
- **1.30.3069** — [release-notes/Archive/1.30.3069/](https://docs.zervicepoint.com/release-notes/Archive/1.30.3069/) · [lokal](../docs-cache/release-notes/Archive/1.30.3069.md)
  - New features and changes · Parallel activity can now contain any combination of activities · Known Issues
- **1.30.3118** — [release-notes/Archive/1.30.3118/](https://docs.zervicepoint.com/release-notes/Archive/1.30.3118/) · [lokal](../docs-cache/release-notes/Archive/1.30.3118.md)
  - New features and changes · New manual task system variables available in email templates · Short description in approval activitiy · To-Do List now uses task short description as title · Issues corrected · Known Issues
- **1.31.3196** — [release-notes/Archive/1.31.3196/](https://docs.zervicepoint.com/release-notes/Archive/1.31.3196/) · [lokal](../docs-cache/release-notes/Archive/1.31.3196.md)
  - New features and changes · *Then* and *Else* in conditional activity · Improved provider activity parameter binding experience · New *Plugins* view in Admin Web · Extended plugins inventory · Changes in AdminWeb related to plugins · Added Z-Api selectors to autocomplete in field javascript editor · Auto-generated identifiers · Terminate and restart orders using WebApi and Powershell · Populate read-only fields with WebApi · Issues corrected · Known Issues
- **1.31.3227** — [release-notes/Archive/1.31.3227/](https://docs.zervicepoint.com/release-notes/Archive/1.31.3227/) · [lokal](../docs-cache/release-notes/Archive/1.31.3227.md)
  - Issues corrected · Known Issues
- **1.32.3257** — [release-notes/Archive/1.32.3257/](https://docs.zervicepoint.com/release-notes/Archive/1.32.3257/) · [lokal](../docs-cache/release-notes/Archive/1.32.3257.md)
  - New features and changes · New menu replacing navigation tags · Intervals and weekday settings in the date/time picker · More auto-generated identifiers · Migration from Azure AD Graph to Microsoft Graph · Issues corrected · Known Issues
- **1.33.3327** — [release-notes/Archive/1.33.3327/](https://docs.zervicepoint.com/release-notes/Archive/1.33.3327/) · [lokal](../docs-cache/release-notes/Archive/1.33.3327.md)
  - New features and changes · Customizable store colors and banner image · Hybrid mode API authentication · Issues corrected · Known Issues
- **1.33.3396** — [release-notes/Archive/1.33.3396/](https://docs.zervicepoint.com/release-notes/Archive/1.33.3396/) · [lokal](../docs-cache/release-notes/Archive/1.33.3396.md)
  - Issues corrected · Known Issues
- **1.34.3476** — [release-notes/Archive/1.34.3476/](https://docs.zervicepoint.com/release-notes/Archive/1.34.3476/) · [lokal](../docs-cache/release-notes/Archive/1.34.3476.md)
  - New features and changes · Static sidebar menu · Service tag navigation · Enhanced role-based REST API authorization · Provisioning system events · WCAG compliance · Added ShortDescription to Task resource in REST API · Performance improvements in activity feed and to-do list · Issues corrected · Known Issues
- **1.34.3480** — [release-notes/Archive/1.34.3480/](https://docs.zervicepoint.com/release-notes/Archive/1.34.3480/) · [lokal](../docs-cache/release-notes/Archive/1.34.3480.md)
  - Issues corrected · Known Issues
- **1.34.3493** — [release-notes/Archive/1.34.3493/](https://docs.zervicepoint.com/release-notes/Archive/1.34.3493/) · [lokal](../docs-cache/release-notes/Archive/1.34.3493.md)
  - Issues corrected · Known Issues
- **1.34.3563** — [release-notes/Archive/1.34.3563/](https://docs.zervicepoint.com/release-notes/Archive/1.34.3563/) · [lokal](../docs-cache/release-notes/Archive/1.34.3563.md)
  - New features and changes · Long description on form fields (Infobubble) · OrderId is now visible in the task details view. · Delegation view in AdminWeb · Change to category pickers (DropDown with data sources) · New System variable System.Service.Draft · Update process performance improvements · Remove Central admin setting from API users view · Remove "Worker Settings" page from worker installer when upgrading · Issues corrected · Known Issues
- **1.34.3799** — [release-notes/Archive/1.34.3799/](https://docs.zervicepoint.com/release-notes/Archive/1.34.3799/) · [lokal](../docs-cache/release-notes/Archive/1.34.3799.md)
  - New features and changes · New, faster Get-function in OrderController.cs WebApi · Discard Draft · Improvements to tasks · Toggle show assignees · Show who completed a task or approval activity in the Order Manager. · Be able to toggle cart on Store level · Possibility to put News on pages · Allow access to LongDescription with Z-API · Upgrade .net projects to 4.8 · Issues corrected · Known Issues
- **1.34.3987** — [release-notes/Archive/1.34.3987/](https://docs.zervicepoint.com/release-notes/Archive/1.34.3987/) · [lokal](../docs-cache/release-notes/Archive/1.34.3987.md)
  - New features and changes · Enhanced authentication with OpenID Connect (OIDC) · Customize your task statuses with colorful buttons · Embed services directly on your pages · Personalize your UserWeb with fonts · Enable or disable search bar in the store · Organize your services in pages with Sorting Index · Filter tasks on status · Improved date validation for News creation and editing · User-friendly error messages · Quick save with ctrl+s · Updated Services dropdown with Deletion Indicator in order history · Workflow Manager restart required · Configuring IIS Machine Key for Zervicepoint AdminWeb on Port 443 · Changes in the Zervicepoint Powershell module · Issues corrected · Known issues
- **1.34.4046** — [release-notes/Archive/1.34.4046/](https://docs.zervicepoint.com/release-notes/Archive/1.34.4046/) · [lokal](../docs-cache/release-notes/Archive/1.34.4046.md)
  - New features and changes · Refresh button in order management modal · Issues corrected · Known issues
- **1.34.4197** — [release-notes/Archive/1.34.4197/](https://docs.zervicepoint.com/release-notes/Archive/1.34.4197/) · [lokal](../docs-cache/release-notes/Archive/1.34.4197.md)
  - New features and changes · Short description displayed on service tiles in UserWeb · Add name and identifier table to JavaScript modal · Custom filtering on service variable in Order Manager · Ability to change position of description for form fields · ADFS login without public access to FederationMetadata.xml · ADFS Configuration Changes · Issues corrected · Known issues
- **1.34.5090** — [release-notes/Archive/1.34.5090/](https://docs.zervicepoint.com/release-notes/Archive/1.34.5090/) · [lokal](../docs-cache/release-notes/Archive/1.34.5090.md)
  - New features and changes · Refresh the order details modal in orders view with the shortkey Ctrl+R · Copy the name of a bound variable by clicking the icon · Fold and unfold all functions in the JavaScript editor · Link to draft in service editor · Download your uploaded Logo and Banner · Access your email template from Send Email Activity · Create your own custom modals in the new Order modal editor · Customizable welcome messages · Solved issues · Moving fields and activities with the same name didn't allow you to save · The identifier table in JavaScript modal didn't display the values in a correct way · Email validation no longer accepts white space in the end or beginning · OIDC Application Id was forced to be a GUID · Search function in table pages stopped working after sorting by a column · Modifications · Changed description position default value and behaviour · "Use cart" is now disabled by default in new services · Banner and logo in UserWeb are now centered
- **1.34.5091** — [release-notes/Archive/1.34.5091/](https://docs.zervicepoint.com/release-notes/Archive/1.34.5091/) · [lokal](../docs-cache/release-notes/Archive/1.34.5091.md)
  - Solved issues · Form editor was very slow · Description position not being changed correctly · Fixed authentication to accept raw group name parsing in Azure SAML
- **1.34.5139** — [release-notes/Archive/1.34.5139/](https://docs.zervicepoint.com/release-notes/Archive/1.34.5139/) · [lokal](../docs-cache/release-notes/Archive/1.34.5139.md)
  - New features and changes · API Users page upgraded to Users page · Quickly navigate to your service through an order · Service version is now displayed in order details · Update provider activities with one click · Refresh button in activity feed · While activity delay seconds now allows a static value · Days, hours and minutes are now hidden when a variable is bound to seconds · Solved issues · You couldn't delete users with favorited services · Changing variable type did not clear default value · You can no longer change variable type on a bound variable · Numbers only fields not working correctly on Firefox · Timeout status now shows correctly in To-Do · You can no longer close the post-order modal before order is done · Specified error message for unauthorized user in task
- **1.34.5140** — [release-notes/Archive/1.34.5140/](https://docs.zervicepoint.com/release-notes/Archive/1.34.5140/) · [lokal](../docs-cache/release-notes/Archive/1.34.5140.md)
  - Upgrade From 1.34.5090, 1.34.5091 · Solved issues · Cannot access a service using a shared process in draft mode · Order events does not show up for services with access groups
- **1.34.5141** — [release-notes/Archive/1.34.5141/](https://docs.zervicepoint.com/release-notes/Archive/1.34.5141/) · [lokal](../docs-cache/release-notes/Archive/1.34.5141.md)
  - Solved issues · Columns in all tables are now aligned correctly · Exporting more than 1000 orders to Excel now works as intended · Zervicepoint now only displays one loading spinner when loading the front page · Zervicepoint no longer allows deletion of email templates used in a draft service · You can now save a workflow with a grouped activity in it · Favorited services getting unfavorited now updates properly · Deleting services used in service blocks on pages is no longer allowed · Updating a copied provider activity from a different store now works as intended
- **1.34.5200** — [release-notes/Archive/1.34.5200/](https://docs.zervicepoint.com/release-notes/Archive/1.34.5200/) · [lokal](../docs-cache/release-notes/Archive/1.34.5200.md)
  - New features and changes · Zervicepoint is now asynchronous · Comments when saving drafts · New Z-function: Z.latinize() · Changed the logic for saved time display · New and modified activities/fields/variables are now highlighted · Added last updated column in orders table · Added buttons for previous and next order in order details · Ability to switch between draft versions · Added service variable value to filter in orders table · See who terminated and/or restarted an order · Apply filters with Return key · Added a warning when copying fields/activities from a different version · Table sizes are now dynamic · Solved issues · Service column in orders table no longer displays "unknown service" sometimes · Set-ZPService now updates the service with description intact · Order list no longer crashes when filtering on a rolled back service version · Copying an activity bound to a scoped variable now correctly clears the field if pasted outside the scope · Inserting and modifiying links in rich text fields (RTF) now works again · ESC key now correctly closes an opened JavaScript editor window · Web Api now allows "only status" option and filters simultaneously · You can no longer try to bind an Api key to temporary users without a valid email adress · Auto complete in the JavaScript editor now works properly
- **1.34.5202** — [release-notes/Archive/1.34.5202/](https://docs.zervicepoint.com/release-notes/Archive/1.34.5202/) · [lokal](../docs-cache/release-notes/Archive/1.34.5202.md)
  - Solved issues · Requested by and Receiver columns in orders table now wrap as intended · Cart is now more responsive when checking out · Web/Powershell Api no longer gives false negatives when creating components
- **1.34.5203** — [release-notes/Archive/1.34.5203/](https://docs.zervicepoint.com/release-notes/Archive/1.34.5203/) · [lokal](../docs-cache/release-notes/Archive/1.34.5203.md)
  - Solved issues · Custom domains now works as intended · Requested by and Receiver columns in orders table now wrap as intended · Cart is now more responsive when checking out · Web/Powershell Api no longer gives false negatives when creating components
- **Release notes** — [release-notes/plugins/active-directory/](https://docs.zervicepoint.com/release-notes/plugins/active-directory/) · [lokal](../docs-cache/release-notes/plugins/active-directory.md)
  - 1.0.2440 · 1.0.1844 · 1.0.1641 · 1.0.1626 · 1.0.1612 · 1.0.1410 · 1.0.1390 · 1.0.1383 · 1.0.1243 · 1.0.1190 · 1.0.1137 · 1.0.1109 · 1.0.1054 · 1.0.1040 · 1.0.990 · 1.0.924 · 1.0.891 · 1.0.711 · 1.0.708 · 1.0.645
- **Release notes** — [release-notes/plugins/assently/](https://docs.zervicepoint.com/release-notes/plugins/assently/) · [lokal](../docs-cache/release-notes/plugins/assently.md)
  - 1.0.2941.0
- **Release notes** — [release-notes/plugins/exchange/](https://docs.zervicepoint.com/release-notes/plugins/exchange/) · [lokal](../docs-cache/release-notes/plugins/exchange.md)
  - 1.0.1970 · 1.0.1863 · 1.0.1632 · 1.0.1374
- **Release notes** — [release-notes/plugins/files-and-folder/](https://docs.zervicepoint.com/release-notes/plugins/files-and-folder/) · [lokal](../docs-cache/release-notes/plugins/files-and-folder.md)
  - 1.0.1723
- **Release notes** — [release-notes/plugins/linkmobility/](https://docs.zervicepoint.com/release-notes/plugins/linkmobility/) · [lokal](../docs-cache/release-notes/plugins/linkmobility.md)
  - 1.0.0
- **Release notes** — [release-notes/plugins/ms-o365/](https://docs.zervicepoint.com/release-notes/plugins/ms-o365/) · [lokal](../docs-cache/release-notes/plugins/ms-o365.md)
  - 1.0.3917 · 1.0.3753 · 1.0.3669 · 1.0.2425 · 1.0.2413 · 1.0.2160 · 1.0.1999 · 1.0.1970 · 1.0.1844 · 1.0.1676 · 1.0.1669 · 1.0.1641 · 1.0.1632 · 1.0.1612 · 1.0.1374
- **Release notes** — [release-notes/plugins/ms-project/](https://docs.zervicepoint.com/release-notes/plugins/ms-project/) · [lokal](../docs-cache/release-notes/plugins/ms-project.md)
  - 1.0.1579
- **Release notes** — [release-notes/plugins/ms-sccm-package/](https://docs.zervicepoint.com/release-notes/plugins/ms-sccm-package/) · [lokal](../docs-cache/release-notes/plugins/ms-sccm-package.md)
  - 1.0.1970 · 1.0.1879 · 1.0.1397
- **Release notes** — [release-notes/plugins/ms-sccm/](https://docs.zervicepoint.com/release-notes/plugins/ms-sccm/) · [lokal](../docs-cache/release-notes/plugins/ms-sccm.md)
  - 1.0.1970 · 1.0.1397 - Initial release
- **Release notes** — [release-notes/plugins/ms-scsm/](https://docs.zervicepoint.com/release-notes/plugins/ms-scsm/) · [lokal](../docs-cache/release-notes/plugins/ms-scsm.md)
  - 1.0.1879 - Initial release
- **Release notes** — [release-notes/plugins/pdf-automator/](https://docs.zervicepoint.com/release-notes/plugins/pdf-automator/) · [lokal](../docs-cache/release-notes/plugins/pdf-automator.md)
  - 1.0.2712 · 1.0.1954 · 1.0.1941 - Initial release
- **Release notes** — [release-notes/plugins/personlookup-swe/](https://docs.zervicepoint.com/release-notes/plugins/personlookup-swe/) · [lokal](../docs-cache/release-notes/plugins/personlookup-swe.md)
  - 1.0.2375 · 1.0.1935 - Initial release
- **Release notes** — [release-notes/plugins/personlookup/](https://docs.zervicepoint.com/release-notes/plugins/personlookup/) · [lokal](../docs-cache/release-notes/plugins/personlookup.md)
  - 1.0.0
- **Release notes** — [release-notes/plugins/productcatalog/](https://docs.zervicepoint.com/release-notes/plugins/productcatalog/) · [lokal](../docs-cache/release-notes/plugins/productcatalog.md)
  - 1.0.2738 · 1.0.2726 · 1.0.2723 · 1.0.2319 · 1.0.2199 · 1.0.2045 · 1.0.2010
- **Release notes** — [release-notes/plugins/scrive/](https://docs.zervicepoint.com/release-notes/plugins/scrive/) · [lokal](../docs-cache/release-notes/plugins/scrive.md)
  - 1.0.0
- **Release notes** — [release-notes/plugins/servicenow/](https://docs.zervicepoint.com/release-notes/plugins/servicenow/) · [lokal](../docs-cache/release-notes/plugins/servicenow.md)
  - 1.0.1397 · 1.0.1381
- **Release notes** — [release-notes/plugins/timezone-and-culture/](https://docs.zervicepoint.com/release-notes/plugins/timezone-and-culture/) · [lokal](../docs-cache/release-notes/plugins/timezone-and-culture.md)
  - 1.0.1397
- **Release History** — [release-notes/release-history/](https://docs.zervicepoint.com/release-notes/release-history/) · [lokal](../docs-cache/release-notes/release-history.md)

## Nedladdningar

- **Active Directory** — [downloads/activedirectory/](https://docs.zervicepoint.com/downloads/activedirectory/) · [lokal](../docs-cache/downloads/activedirectory.md)
- **Assently E-Sign** — [downloads/assently/](https://docs.zervicepoint.com/downloads/assently/) · [lokal](../docs-cache/downloads/assently.md)
- **Exchange** — [downloads/exchange/](https://docs.zervicepoint.com/downloads/exchange/) · [lokal](../docs-cache/downloads/exchange.md)
- **Files and folders** — [downloads/files-and-folder/](https://docs.zervicepoint.com/downloads/files-and-folder/) · [lokal](../docs-cache/downloads/files-and-folder.md)
- **LinkMobility** — [downloads/linkmobility/](https://docs.zervicepoint.com/downloads/linkmobility/) · [lokal](../docs-cache/downloads/linkmobility.md)
- **Office 365** — [downloads/ms-o365/](https://docs.zervicepoint.com/downloads/ms-o365/) · [lokal](../docs-cache/downloads/ms-o365.md)
- **SCCM Package** — [downloads/ms-sccm-package/](https://docs.zervicepoint.com/downloads/ms-sccm-package/) · [lokal](../docs-cache/downloads/ms-sccm-package.md)
- **SCCM** — [downloads/ms-sccm/](https://docs.zervicepoint.com/downloads/ms-sccm/) · [lokal](../docs-cache/downloads/ms-sccm.md)
- **SCSM** — [downloads/ms-scsm/](https://docs.zervicepoint.com/downloads/ms-scsm/) · [lokal](../docs-cache/downloads/ms-scsm.md)
- **PDF Automator** — [downloads/pdf-automator/](https://docs.zervicepoint.com/downloads/pdf-automator/) · [lokal](../docs-cache/downloads/pdf-automator.md)
- **Person Lookup(SWE)** — [downloads/personlookup-swe/](https://docs.zervicepoint.com/downloads/personlookup-swe/) · [lokal](../docs-cache/downloads/personlookup-swe.md)
- **PersonLookup** — [downloads/personlookup/](https://docs.zervicepoint.com/downloads/personlookup/) · [lokal](../docs-cache/downloads/personlookup.md)
- **Product Catalog** — [downloads/product-catalog/](https://docs.zervicepoint.com/downloads/product-catalog/) · [lokal](../docs-cache/downloads/product-catalog.md)
- **Scrive E-Sign** — [downloads/scrive/](https://docs.zervicepoint.com/downloads/scrive/) · [lokal](../docs-cache/downloads/scrive.md)
- **ServiceNow** — [downloads/servicenow/](https://docs.zervicepoint.com/downloads/servicenow/) · [lokal](../docs-cache/downloads/servicenow.md)
- **Timezone and Culture** — [downloads/timezone-and-culture/](https://docs.zervicepoint.com/downloads/timezone-and-culture/) · [lokal](../docs-cache/downloads/timezone-and-culture.md)
- **Zerflow** — [downloads/zerflow/](https://docs.zervicepoint.com/downloads/zerflow/) · [lokal](../docs-cache/downloads/zerflow.md)
- **Zervicepoint** — [downloads/zervicepoint/](https://docs.zervicepoint.com/downloads/zervicepoint/) · [lokal](../docs-cache/downloads/zervicepoint.md)
