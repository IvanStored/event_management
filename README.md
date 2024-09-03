# Event Management API


The primary goal of this task is to create a Django-based REST-Api that manages
events (like conferences, meetups, etc.). The application will allow users to create,
view, update, and delete events. It should also handle user registrations for these
events.

## Installation and running

```bash
git clone https://github.com/IvanStored/event_management.git
cd event_management
*create .env file (.env.sample for example)*
docker compose up
```
## Admin creds:
admin:admin_pasword

## Non-admin creds:
johndoe:not_admin

## API docs endpoint:
- api/schema/swagger-ui/

## Features

- JWT authenticated
- CRUD for events instances
- Basic user registration
- Registration for event
- Filters for events
- sending email notifications to users upon event registration.
