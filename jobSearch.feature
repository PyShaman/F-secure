Feature: Job search

    Scenario: User is meant to navigate to Careers tab and search for specific job offer
        Given User is on main page
        When User navigates to "Careers" page
        Then User is on "Careers" page
        When User clicks on "See our open positions" button
        Then User is navigated to list of all jobs
        When User selects "Poznań" from drop down menu
        And User search for "Quality Engineer"
        And User clicks on "View job"
        Then New browser tab with "Quality Engineer" job details opens