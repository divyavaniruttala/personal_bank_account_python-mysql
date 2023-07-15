# personal_bank_account_python-mysql
1.INTRODUCTION    
Personal Bank Account: An individual account means a bank account that is only used for non-business activities. The distinction is made between personal accounts and other accounts in banking and accounting because different account types have different implications and treatments. In a business account there are probably many users that are extracting from a large pool of money for the purpose of running a business.
For a personal account, there should only be one person depositing and withdrawing money and therefore security measures will be in place to make sure the right person is accessing the funds. Personal accounts are often kept completely separate from business and joint accounts because they are completely in the interest of one user rather than many. Functioning of a Bank is among the more complicated of corporate operations. Since Banking involves dealing directly with money it becomes difficult. So, this application was made to make all that process easy.
This application provides you convenience and basic banking transactions such as transferring funds between accounts can easily be done any time of the day or night, seven days a week.is fast and efficient. Funds can be transferred between accounts almost instantly. You can open and close a number of different accounts online.
RULES THAT GOVERN THIS PROJECT:
1)	The account numbers cannot be null i.e., they cannot take null values.
2)	All the customers of the bank have a unique account number.
3)	The customers must have a minimum account balance of Rs.1000.

OBJECTIVE

The Personal Bank Account is a Database Project which is more efficient, fast, reliable, user friendly. Convenience is a major advantage. Over and above the proposed system does not have any possibility of data loss during processing. This Personal Bank Account project will serve as a useful approach to data base dialogue box to deposit and withdraw the money as well as the balance enquiry for the person. It serves as a helpful approach for the users. It provides easy way of the deposit and withdrawal of the money. It reduces the time taken by the user to save the money. Thus, the project is the user-friendly approach.
   
  2.TERMINOLOGY USED IN THIS PROJECT

1.	INTEGER:  One optional sign character (+ or -) followed by at least one digit from 0-9. Leading and trailing blanks are ignored. No other character is allowed.

2.	VARCHAR:  A VARIABLE length string (can contain letters, numbers, and special characters). The size parameter specifies the maximum string length in characters – can be from 0 to 65535. It is used to store alpha numeric values. By default, SQL server sets the size to 50 characters range.


3.	DATE: Store a date only. No parameters are required when declaring a DATE data type. It stores dates from January 1, 0001 to December 31, 9999.


4.	Mysql Connector: This database application is made of Python and Mysql. Python can be used in database applications. MySQL Connector enables Python programs to access MySQL databases.



    3.  DATA REQUIREMENTS


ENTITIES:

	CUSTOMERS
	BANK
	AMOUNTS

ATTRIBUTES:

	CUSTOMERS -- 	Customer Name
			            Account Number
			            Date of Birth
				Address

	BANK        --       	Bank Name
				IFSC Code
				Bank ID
				Bank Address

	AMOUNTS -- 	Account number
				Customer Name
				Total Amount


RELATIONSHIPS – CARDINALITY

	BANK has CUSTOMERS
	BANK maintains AMOUNT
	BANK offers LOANS
	CUSTOMERS can DEPOSIT
	CUSTOMERS can WITHDRAWAL


4.ENTITY RELATIONSHIP -DIAGRAM



ER Diagram stands for Entity Relationship Diagram, also known as ERD is a diagram that displays the relationship of entity sets stored in a database. In other words, ER diagrams help to explain the logical structure of databases. ER diagrams are created based on three basic concepts: entities, attributes and relationships.ER Diagrams contain different symbols that use rectangles to represent entities, ovals to define attributes and diamond shapes to represent relationships.
   Prime reasons for using the ER Diagram:
	Helps you to define terms related to entity relationship modeling
	Provide a preview of how all your tables should connect, what fields are going to be on each table
	Helps to describe entities, attributes, relationships
	ER diagrams are translatable into relational tables which allows you to build databases quickly
	ER diagrams can be used by database designers as a blueprint for implementing data in specific software applications
	The database designer gains a better understanding of the information to be contained in the database with the help of ERP diagram
	ERD Diagram allows you to communicate with the logical structure of the database to users.

 

