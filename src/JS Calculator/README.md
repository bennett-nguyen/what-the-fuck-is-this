# JS Calculator

A simple web calculator built using HTML, JS and CSS.

# How Did I Came Up With The Idea?

I learnt web development (actually, messing around with frontend dev) for 2 months, and then I decided to build this calculator in order to train my HTML programming skills. The design and logic is fairly simple to comprehend. I drew some figures during the development of the calculator, you can read and understand the logic while also looking at the image to imagine how this works:

First, I drew a frame called "container" and it encapsulates the expression field and the buttons field

![image](https://raw.githubusercontent.com/bennett-nguyen/what-the-fuck-is-this/main/image/figure_1.jpg)
<br>

The expression field display the expression that the user entered while the buttons field helps the user enter what they want to enter for doing calculations (kinda self-explanatory)

![image](https://raw.githubusercontent.com/bennett-nguyen/what-the-fuck-is-this/main/image/figure_2.jpg)
<br>

After that, I added buttons, logic and stuff to the calculator (HTML for the UI and JS for the logic)
<br>
<br>
About the logic: When the user press a button (any button except for the functional button like the AC button or "=" button), a string that corresponded to the button they pressed will be appended to the "expression" string, it will then be displayed on the expression field. When the user hit the "=" functional button, the "expression" string will be computed using the `eval` function in JS and displayed to the expression field.

![image](https://raw.githubusercontent.com/bennett-nguyen/what-the-fuck-is-this/main/image/figure_3.jpg)
<br>

My calculator was missing some CSS so I added them to make the calculator look better (I'm not a designer so don't blame me for the bad designing)
<br>

![image](https://raw.githubusercontent.com/bennett-nguyen/what-the-fuck-is-this/main/image/epik_css.jpg)
<br>

I tried fixing some bugs I found and added more features like keyboard inputs, previous expression preview, etc. And voilà, the calculator is completed.

![video](https://raw.githubusercontent.com/bennett-nguyen/what-the-fuck-is-this/main/image/epik_calculator.mp4)
<br>

# What's Bad With The Code?
CSS code seems fine to me, but the JS's is pretty DRY, implicit and LONGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG. Also, the buttons field got overflowed and the reason behind it is... I don't really know ¯\\\_(ツ)_/¯