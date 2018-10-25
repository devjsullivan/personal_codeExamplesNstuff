import sys
import pdb
import re

# -*- coding: utf-8 -*-
"""
Comcast Pre-Interview Questionnaire - Python

Interviewing candidates takes a lot of time, and time is valuable for all of us.
If you are as serious about working for Comcast as we are about working with great people,
please take the time to fill out this questionnaire. We devised these questions as a test of
skills we consider primary and fundamental. If you find yourself taking much more than
the suggested completion time to answer the questions, then Comcast might not be a good
fit at this time. The in-person interview questions will be more difficult, and hopefully
a better test of your programming skills.

Instructions:
    * Read and work on the problems in a text/html editor. It will make a lot more sense that way.
    * Do not use any frameworks or external libraries.
    * Use your own style of programming.
    * Work on this alone. Feel free to use google or any reference material you have.
    * If you can't solve a problem, comment on it.

"""

"""
Ranking Questions:
==================

Rate yourself on the following technologies on a scale of 1-10.
You may be asked to justify these answers in an interview.
            
    1 - Beginner (I don't really know that)
    4 - Intermediate (I can work without help)
    6 - Advanced (People come to me for help in esoteric or hard problems)
    8 - Industry Expert (People outside my office see me as an expert)
    10 - Spec/Language Author or Primary Contributor.
            
Python language: 4
Python web frameworks: 1
Test frameworks: 1
Asynchronous programming: 1
Build tools: 4 
Git/CI tools: 4
Other programming languages: 6

"""

"""
DevOps Questions:
=================

Question 1: How do you use source control to manage releases? How would you handle an emergency release?
--------------------------------------------------------------------------------------------------------


Only release when all significant source is checked in/ up to date.  Use CM to check for diffs in source.
Release delivery script should append Emergency string to emergency released libraries/objects/deliveries.  Emergency release branch or view should be snapped/dated/tagged via the CM tool.



Question 2: List the testing frameworks you have written tests in:
------------------------------------------------------------------


All in-house at Lockheed Martin



Question 3: As an API developer, describe three performance and security concerns you need to deal with and how you address them.
---------------------------------------------------------------------------------------------------------------------------------

Check and limit processing for large list sizes or values, add a MAX input parameter to suggest implementation of it in definition,
use default values



"""

"""
Personal Development:
=====================

Question 1: Share something you've learned in the past month.
-------------------------------------------------------------


A piece of the southwestern coast of NJ is actually part Delaware (Finn's Point National Cemetery): 
https://www.onlyinyourstate.com/new-jersey/nj-delaware-border/

C++ has a std reverse function for containers (e.g. vectors)


Question 2: What is an area of software development that you want to grow in?
-----------------------------------------------------------------------------


**Replace this comment with your answer**

.NET, Amazon Web Services, Java, iOS, Android

"""


"""
Python Questions:
=================

The Python portion of the questionnaire should be completed within 90 minutes.

"""

"""
Question 1: Write a Python function to check if a number is prime or not.
-------------------------------------------------------------------------

"""


def is_prime(num):
    """
    This function takes a number as argument and checks if it is prime or not.

    Args:
        num (int): an integer number.
        
    Returns:
        bool: The return value. True if prime number, False otherwise.

    Examples:
        >>> is_prime(3)
        True

        >>> is_prime(4)
        False

    **Write your code below**
   """
    ret = True;
    numStr = str(num);
    if num <= 1:
        """
            See https://primes.utm.edu/notes/faq/one.html, 1 is NOT prime:
        By definition of prime!
        The definition is as follows. 
        An integer greater than one is called a prime number if its only positive divisors          (factors) are one and itself. 
        """
        ret = False;
        return ret;
    
        # 2 will bypass the following while loop and ret will rmain True
    else:
        factor = 2;
        # This is kind of a brute force method, I'm sure there is probably somthing more
        #      elegant - cue Mathematician failure sound
        while factor < num:
            # check for any divisors of num
            if num % factor == 0:
                ret = False;
                return ret;
                # next possible divisor
            factor += 1;

    return ret;



"""
Question 2: Write a Python function to convert RFC 2822 date format to ISO 8601 format.
---------------------------------------------------------------------------------------

"""


def convert_rfc2822_to_iso8601(rfcdate):
    """
    This function takes a RFC 2822 formatted date string
    and converts it to a ISO 8601 formmated date string.

    Args:
        rfcdate (str): RFC 2822 formatted date string

    Returns:
        str: The return value. ISO 8601 formatted date string

    Examples:
        >>> convert_rfc2822_to_iso8601('Fri, 21 Nov 1997 09:55:06 -0600')
        '1997-11-21T09:55:06-06:00'

        >>> convert_rfc2822_to_iso8601('Tue, 26 Jun 2018 04:00:00 UTC')
        '2018-06-26T04:00:00Z'  # or '2018-06-26T04:00:00+00:00'

    **Write your code below**
    """
    m = re.search('\w+\s*,\s*([\w\s]+)[\s,]+(.*)', "Fri, 21 Nov 1997 09:55:06 -0600")
    "test"
    if m:
        date = m.group(1);
        time = m.group(2);
        md = re.search('([0-9]+)\s+([\w]+)\s+([0-9]+)', date);
        mo = 0;
        yr = 1971;
        try:
            yr = md.group(3);
        except:
                print("Year not found via regex");
        try:
            mth = md.group(2);
        except:
            print("Month not found via regex");
        try:
            day = md.group(1);
        except:
            print("Day not found via regex");
        if mth == "Jan":
            mo = 1;
        elif mth == "Feb":
            mo = 2;
        elif mth == "Mar":
            mo = 3;
        elif mth == "Apr":
            mo = 4;
        elif mth == "May":
            mo = 5;
        elif mth == "Jun":
            mo = 6;
        elif mth == "Jul":
            mo = 7;
        elif mth == "Aug":
            mo = 8;
        elif mth == "Sep":
            mo = 9;
        elif mth == "Oct":
            mo = 10;
        elif mth == "Nov": 
            mo = 11;
        elif mth == "Dec":
            mo = 12;
    isoStr = str(yr) + "-" + str(mo)  + "-" +  str(day)  + "T" + str(time.replace(" ", ""));
    return isoStr;
""" 
Question 3: Write a Python class to implement Linked List.
----------------------------------------------------------

Implement a Linked List class that supports the following operations:
    * Insert: inserts a new data node into the list
    * Size: returns size of list
    * Search: searches list for a node containing the requested data and returns that node if found, otherwise raises an error
    * Delete: searches list for a node containing the requested data and removes it from list if found, otherwise raises an error
    * Generator: returns a generator that returns the next data object in the linked list

"""


class LinkedList(object):
    def __init__(self, data, head=None):
        """
        **Write your code below**
        """
        self.value = data;
        self.next = None;

        self.cardinality = 0;

        
    def insert(self, data):
        """
        **Write your code below**
        """
        new_item = LinkedList(data);
        new_item.cardinality = self.size() + 1;
        new_item.next = self.next;

        self.next = new_item;

    def size(self):
        """
        **Write your code below**
        """
        counter = 1;
        itrNode = self;
        while itrNode.next:
            counter = counter + 1;
            itrNode = itrNode.next;
            
        return counter;

    def search(self, data):
        """
        **Write your code below**
        """
        itrNode = self;
        while str(itrNode.value) != str(data):
            itrNode = itrNode.next;
            
        return itrNode;

    def delete(self, data):
        """
        **Write your code below**
        """
        self.next = data.next;

    def generator(self):
        """
        **Write your code below**
        """
        return self.next;

    def print(self):
        itrNode = self;
        while itrNode.next:
            print("The " + str(itrNode.cardinality) + "th" + " item in the list has value " + str(itrNode.value));
            itrNode = itrNode.next;
            
        return;

""" 
Question 4: Write a Python test program using the classes and function above.
-----------------------------------------------------------------------------

Write a test program that uses all functions and LinkedList class defined in above questions.
For example, insert random numbers and RFC 2822 formatted date strings to the LinkedList,
print the initial size of the list, use the generator to convert date string to ISO format,
delete all prime numbers from the list, and print the final size of the resulted list.

Example:
    In the end, this file should be an executable Python program that can demonstrate
    all your answers to the Python programming questions listed above.::

        $ python interview_questionnaire.py

"""


def main():
    """
    **Write your code below**
    """
    
    arr = { 0, 2, 1, 3, 5, 10, 12, 20 }
    for a in arr:
        aStr = str(a);
        if is_prime(a):
            print(aStr + " is prime.");
        else:
            print(aStr + " is not prime.");


    array = list([0, 2, 1, 3, 5, 10, 12, 20]);
    array;
    print("start");
    ll = LinkedList(0);
    ll.insert(1);
    ll.insert(2);
    ll.insert(3);
    ll.insert(5);
    ll.insert(10);
    ll.insert(12);
    ll.insert(20);

    sz = ll.size();
    print("My Linked List of size " + str(sz)+ " is: ");
    ll.print();
    lg = ll.generator();
    print("The generator from my Linked List is of size " + str(lg.size())+ " and is: ");
    lg.print();
    
    inVal = input("Please enter a value to search:");
    inSearch = ll.search(inVal);
    inGen = inSearch.generator();
    sz = str(inGen.size());
    print("The rest of my Linked List after your value of " + str(inVal) + " is of size " + sz + " and is:");
    inGen.print();
    
    rfcStr = "Fri, 21 Nov 1997 09:55:06 -0600";
    print("Testing date conversion from RFC2822 \"" + str(rfcStr) + "\" to iso8601: \"" + convert_rfc2822_to_iso8601(rfcStr) + "\"");
    
if __name__ == "__main__":
    main()
            # sys.stdout.write("try "  + str(v) + " ");


"""
Thank you for completing this questionnaire!
We'll take a look at what you submitted and get back to you soon.
If you have any comments or suggestions please let us know below.

**Replace this comment with your additional comments**

"""