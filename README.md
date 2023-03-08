<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>Writing Scheduler README</h1>
	<p>This program allows the user to calculate the expected number of pages to write each day for a given date range and writing schedule. The program creates a graphical user interface (GUI) using the tkinter library and the tkcalendar module for selecting the start and end dates.</p>

<h2>Requirements</h2>
<ul>
	<li>Python 3.x installed</li>
	<li>Required modules: tkinter, ttk, tkcalendar</li>
</ul>

<h2>Usage</h2>
<ol>
	<li>Run the program by executing the Python script.</li>
	<li>Select the start and end dates using the calendar widgets.</li>
	<li>Enter the writing schedule in pages per day.</li>
	<li>Click the "Calculate Pages" button to generate the expected page numbers.</li>
	<li>The expected page numbers will be displayed in the output text box.</li>
</ol>

<h2>Code Overview</h2>
<p>The program consists of a single function <code>calculate_pages</code> that is executed when the "Calculate Pages" button is clicked. The function retrieves the start and end dates and the writing schedule from the GUI widgets, calculates the number of days between the start and end dates, and loops through each day to calculate the expected page number.</p>

<p>The expected page number for each day is based on whether the day is a weekday or a weekend, and whether it is the first or second page of a two-page spread or the third page of a three-page spread.</p>

<p>The program uses the tkinter and ttk modules to create the GUI, and the tkcalendar module to create the calendar widgets.</p>

<h2>Author</h2>
<p>This program was created by Lakhan Raut.</p>
</body>
</html>
