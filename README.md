
# My Car Service Web Application
#### Video Demo:  [Click here for video demo](https://youtu.be/wuNVpyZ4Fog)
#### Description:  Creating a web application which can track and monitor my car service record

> Name: Yap Weng Kiad
>
> Email: wengkiadyap@gmail.com
>
> Date: 3rd Dec 2023
>
> Country: Malaysia / Kuala Lumpur

This web application was created using flask and consists of the following function:

 - Display all previous service record
 - Schedule next service item – e.g. recommend what item need to be service for next (based on service interval recommended by car maker)
 - Have flexibility to add / remove service item
 - Display confirmation page of list of service items and price, and estimate total cost
 - Submit service record and stored this entry to database
 - Delete previous service record for wrong entry
 - Display response page to indicate successful to add / delete entry

All service interval refer to:
![Car maker schedule](https://i.imgur.com/hIDOrs0.png)

**All function explained**

>  - Display all previous service record
>  ![function explained 1](https://i.imgur.com/9eCVU3q.png)
> All service record was input into sqlite3 database, and added date time column for easy monitoring
> Use flask application to connect sqlite3 to retrieve previous record, and display on index page


> - Schedule next service item – e.g. recommend what item need to be service for next (based on service interval recommended by car maker)
> ![function explained 2](https://i.imgur.com/pipSuUd.png)
> ![function explained 3](https://i.imgur.com/GTjTPFU.png)
> Refer to the Periodic service maintenance schedule provided by original car maker, calculate service interval for each service item
> e.g. Engine oil – service every time
> e.g. Spark plug – every 3 time service, need change spark plug
> e.g. Air filter – every 2 time service, need change air filter
> Kindly take note first service in the Periodic service maintenance schedule provided by original car maker was excluded, due to first service is run in period service which only change engine oil, engine oil filter and drain plug gasket, it is not part of the periodic service and hence excluded from the interval calculation. interval calculation must start from 2nd service
> python will generate a list of recommend next service item
> Use jinja syntax to prechecked the form in next service for recommended next service item


> - Have flexibility to add / remove service item
> ![function explained 4](https://i.imgur.com/taIztOt.png)
> in real life situation, part replacement could be done early or postponed, this function provide the flexibility to alter service item
> achieve through check or uncheck the form

> - Display confirmation page of list of service items and price, and estimate total cost
> - Submit service record and stored this entry to database
> ![function explained 5](https://i.imgur.com/JMbVjEK.png)
> Confirmation page is to let use confirm first, before add the entry to database
> list of item with price shown was displayed by using python dictionary function
> From confirmation page also can estimate total cost
> Once confirmed, will add entry to database

 >- Delete previous service record for wrong entry
 >![function explained 6](https://i.imgur.com/ID87kDM.png)
 > only allowed to detele latest record, this is important to preserve python calculation function.
 > for e.g. if latest service record is no. 17, but recorded no.16 was deleted, then the python calculation function to recommend next service item will be disturbed, hence, it designed to allowed delete one single record from latest entry only
 > However, user can revisit this route again to continue to delete early record if necessary

 >- Display response page to indicate successful to add / delete entry
 >![function explained 7](https://i.imgur.com/JLklXAi.png)
 > Added redirect function to be user friendly

Thank you!
