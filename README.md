# one eleven

<img src="https://raw.githubusercontent.com/closeair/sundowners-fc/dev/static/img/logo.png" width="100"/>

Suite for the day to day operation of the Sundowners Flight Club, et al.

## What is this?

The sundowners-fc code base was developed as part of the preparation for the Sundowners Flight Club as well as extracted from a solution developed for the Richmond Pilots Corporation, a flight club originally based at Miller Field in Staten Island but later moved to KLDJ when Miller Field was closed in the late 1960s.

It leverages the Django Framework to provide mostly the day to day operations of a flight club or school. Specifically, it provides member management, scheduling and management of aircraft as well as invoicing, etc.

## What is it not?

It is not a traditional 'website' to post information about your club or pictures of your last gathering. That said there is a basic information page that is customizable to some extend and we suggest that if you want something more social that you use a facebook page, etc, tools that are developed specifically for socializing. You can link to those pages (facebook, instagram, twitter, slack, etc) from this basic information page.

### Types of Users

* Public, non-logged-in person able to see the introduction page for your club and submitted a membership application.
* Member, able to log in but limited permissions to schedule, vote, upload, etc.
* Staff, same as member but able to access the admin pages, see membership applications, etc.

### Current Features

* Member management
* Insurance Surveys
* Aircraft Management and Scheduling
* Invoicing with optional, limited payment gateway for online payments.
* Ability to create Motions and Vote on them
* Ability to write Custom Surveys to request input from members.
* Public / Internal document support
* Support for meeting minutes and attendance.
* Basic information pages (home, faq, fleet, resources, social media links, etc)
* Customization wizard for choosing your own logos and colors

## Getting Running

Copy the enviroment file:

    $ cp .env.example .env

Fill in your specific details and migrate:

    $ ./manage.py migrate

Now create a default superuser:

    $ ./manage.py createsuperuser

And start:

    $ ./manage.py runserver

The first time you start the application you will brought through a configuration form that will gather some details regarding your organization. This should be fairly self explanatory. The resulting information gathered will be the basis of the non-logged-in home page. The admin UI is more or less the default Django admin and should be intuitive. That said, for the sake of clarity this is a brief overview of available options.


## Testing

If you plan to develop the code base and wish to use TDD, run the test suite with the following:

    $ ./manage.py test


## Lineage
The founder of this project (and the Sundowners Flight Club) was a member of the US naval squadron VF-111 Sundowners (1956-95), as serves as the direct lineage of the Sundowners legacy.

Illegitimi Non Carborundum.
