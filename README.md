# Log Analysis Project

This log analysis project is simple console run script used to communicate with a database and query specific information about that database. The database named 'news' contains tables about that newspapers authors, and articles, as well as a logs table which tracts the websites activity. The script presented in the Log Analysis seeks to answer 3 main questions: 
1. What are the most popular articles?
2. Who are the most popular authors?
3. On which days did more than 1% of requests lead to errors? 

The script answers these questions by interacting with a sql database. After running through the demo, you too will be able to query this database to answer these questions and any other you can think of.

## Clone Repository

You can clone this git repository from your terminal by entering:

`git clone https://github.com/osa10928/Udacity_FullStack_Log_Analysis.git`

(You can copy/paste the url by clicking the clone button on the top right)

This repository only includes the script that runs on the console and  queries the database and sample output. **The repository does not include the sql file** needed to create the database due to size contraints. The actual file is available [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) thanks to the team at Udacity Fullstack Nanodegree.

## Specifications

The script is written in python3.
`'python3' >= '3.5.2'`

The database used for this analysis is postgresql version 9.5.9.

 `'psql' >= '9.5.9'`


### Recommended Installation

Though this analysis is perfectly capable of being run on you local environment, its recommended that it be run on a Virtual Machine (VM). This assures the correct environment is generated for this exercise. Not to mention once the software used to launch and operate the VM is installed, any other development environment can be configured and launched without having to create that specific environment on your local machine.

#### Install Virtual Box

Virtual Box is the software that runs the virtual machine. You can install Virtual Box from there [website.](https://www.virtualbox.org/wiki/Downloads) Be sure to download the package for your operating system.
**Ubunutu Users** are recommended to use the Ubuntu Software Center to download and install their package.

### Install Vagrant

Vagrant is used to configure the VM and allows for files to be shared between your local machine and the VM. Download and install your operating system's package [here.](https://www.vagrantup.com/downloads.html)


### Launch Your Virtual Machine

In normal cases you would initiate your VM by going to the directory of your choice and calling

`vagrant init`

If a "VagrantFile" were located in that directory, Vagrant would launch with the configerations specified by that file. If a file is not present Vagrant would attempt to download a Vagrant File and configure itself. 

The vagrant website recommends running:

`vagrant init hashicorp/precise64`

to initatiatize a default, fully functioning VM running Ubuntu 12.04 LTS 64-bit.

For the sake of this tutorial a vagrant file directory is availabe for download [here.](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) Alternatively, you can fork the repository from github by clicking [here.](https://github.com/udacity/fullstack-nanodegree-vm) This directory comes fully equiped with a VagrantFile that will set up a VM environment that will allow us to carry out this exercise (and is brought to you by Udacity). Once downloaded cd into the 'vagrant' directory and call

`'vagrant init`

Once Vagrant has initialized, run the command

`vagrant up`

to build the VM, and

`vagrant ssh`

to log into the machine. Congradulations!! You've downloaded, installed, and lauched your Virtual Machine!! To access the shared files in the 'vagrant' directory on your local machine, run 

`cd /vagrant`

from your VM. You now have access to local files on your VM machine.

## Run Demo

The Log analysis is a command line script meant to query the database and return answers to 3 questions, namely:
1. What are the most popular articles?
2. Who are the most popular authors?
3. On which days did more than 1% of requests lead to errors?

To run the demo follow these steps:

1. Setup correct environment and run `python3 --version` and `psql --version` to check that you meet the software requirements.
2. Clone repository and download the sql database file. Place them in the same directory. If running script from a VM, place the directory in the VM directory (The 'vagrant' directory if you have configured you're environment using the VagrantFile I've made available above).
3. Cd into the vagrant directory from your virtual machine and into the "log-analysis" directory. In this is the demo file "newsdatalog.py" which is the actual script, "newsdata.sql" which is the script needed to generate the database, and "sample-output.txt" which is just a text file containing sample output.
4. Create the database using postgresql. Run 

`psql -d news -f newsdata.sql`

5. Finally run the python file with

`python3 newslogdata.py`

to get the answers to the 3 target questions of the demo.

## Create Your Own Script!!

In reality any query can be run on this database with a little python code. Heres how to run your queries:
1. Create and open a new python file titled 'myqueries.py' within the directory the same directory as the sql file.
2. import psycopg2 with an 'import psycopg2' statement. Psycopg2 is the module used to connect and interact with the database.
3. Connect to the database with this line:

`db = psycopg2.connect(database=DBNAME)`

where 'DBNAME' is the name of the database (in this example DBNAME='news').
4. To query a database a cursor object must be used. Create your cursor object with:

`c = db.cursor()`

5. Execute your query 
`c.execute(Query)`
where Query is an sql query string. Here's and example from the demo:

`c.execute(
    "SELECT path, count(path) FROM log GROUP BY path HAVING path like '/article%' ORDER BY count desc LIMIT 3")`

6. Finally you can access your query object by running:

`top3 = c.fetchall()`


Alternativly you can run

`top1 = c.fetchone()`


to fetch one object.
7. The query in now stored into whatever variable you provided and is free to be manipulated however you want.

**Caveat**
It is recommended you create a query response that is as close to your desired finished product as possible. This benefits of this are twofold:
1. It allows the database to do the heavy lifting. Instead of looping through large queries these changes, the database can do it a decreased time/space cost.
2. Letting the database do the lifting makes coding easier (and less error prone) for all of us!

## Create Queries

Its possible to run queries against the database without running python script. From your console create the database by running:

`psql -d news -f newsdata.sql`

Access the database by running:

`psql -d news`

This will put you within the psql console. From here you can run any sql query that is accepted by postgresql. To examine the database run

`\d`

Use

`\dt` 

To examine the tables. 


## Contibution

Thanks again to the team at Udacity Fullstacks Nanodegree for providing to code needed to create the database as well as the VagrantFile needed to initiate the Virtual Machine environment!!
