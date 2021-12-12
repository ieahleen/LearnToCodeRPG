init python:

    general_questions = [

        QuizQuestion(
        question="What is a bug?",
        true="An error in a computer program that causes it to generate an incorrect or unexpected result or output.",
        false=["A programming paradigm. ", "A programming structure that repeats a block of code a given number of times", "This concept is not related to programming at all."],
        explanation="A {b}bug{/b} is an error in a computer program that causes it to generate an incorrect or unexpected result or output. The process of finding and fixing bugs is known as {b}debugging{/b}.",
        learn_more_url="https://en.wikipedia.org/wiki/Software_bug",
        difficulty=1
        ),
        QuizQuestion(
        question="The process of finding and fixing bugs in a computer program is known as...",
        true="Debugging",
        false=["Encapsulation", "Abstraction", "Looping"],
        explanation="Debugging is the process of finding and fixing bugs in a computer program. ",
        learn_more_url="https://en.wikipedia.org/wiki/Debugging",
        difficulty=1
        ),
        QuizQuestion(
        question="Select the type of loop that repeats a sequence of instructions an unknown number of times while a condition is True. ",
        true="While loop",
        false=[" For loop", "Infinite loop", "Circular loop"],
        explanation="While loops repeat a block of code an unknown number of times while a condition is True and they stop when the condition is False. ",
        learn_more_url="https://www.freecodecamp.org/news/python-while-loop-tutorial/",
        difficulty=2
        ),
        QuizQuestion(
        question="What type of loop is used to repeat a block of code a known number of times?",
        true="For loop",
        false=["While loop", "Infinite loop", "Triangular loop"],
        explanation="For loops repeat a block of code a known number of times, so we can use it when we know in advance how many iterations we need to run to complete a task. ",
        learn_more_url="https://www.freecodecamp.org/news/javascript-loops-explained-for-loop-for/",
        difficulty=2
        ),
        QuizQuestion(
        question="What is an infinite loop?",
        true="A loop that will continue endlessly unless an external intervention stops its execution. ",
        false=["A loop that only completes two iterations.", "A loop that cannot be stopped, even with external intervention. ", "A loop that never runs."],
        explanation="An infinite loop is a loop whose condition is always true, so it would continue running endlessly unless there is some external intervention to stop it.",
        learn_more_url="https://www.freecodecamp.org/news/python-while-loop-tutorial/",
        difficulty=2
        ),
        QuizQuestion(
        question="The process by which a function calls itself directly or indirectly is known as...",
        true="Recursion",
        false=["Looping", "Encapsulation", "Decomposition"],
        explanation="Recursion is the process by which a function calls itself directly or indirectly during its execution. This works for problems that can be solved by solving smaller instances of the same problem. ",
        learn_more_url="https://www.freecodecamp.org/news/understanding-recursion-in-programming/",
        difficulty=2
        ),
        QuizQuestion(
        question="What is an algorithm?",
        true="A sequence of detailed step-by-step instructions to complete a task.",
        false=["A programming paradigm.", "A Python module.", "A web development framework."],
        explanation="An algorithm is a sequence of detailed step-by-step instructions to complete a task.",
        learn_more_url="https://www.freecodecamp.org/news/algorithms-explained-what-they-are-and-common-sorting-algorithms/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does IDE stand for?",
        true="Integrated Development Environment",
        false=["Internal Development Environment", "Integrated Design Environment", "International Development Experimentation"],
        explanation="IDE stands for Integrated Development Environment.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-an-ide-in-programming-an-ide-definition-for-developers/",
        difficulty=1
        ),
        QuizQuestion(
        question="A special symbol used to perform arithmetic or logical computations is known as...",
        true="Operator",
        false=["Operand", "", ""],
        explanation="A special symbol used to perform arithmetic or logical computations is known as operator.",
        learn_more_url="https://en.wikipedia.org/wiki/Operator_(computer_programming)",
        difficulty=1
        ),
        QuizQuestion(
        question="The values that an operator operates on are known as...",
        true="Operands",
        false=["Operators", "", ""],
        explanation="The values that an operator operates on are known as operands.",
        learn_more_url="https://en.wikipedia.org/wiki/Operand",
        difficulty=1
        ),
        QuizQuestion(
        question="The rules that determine the correct structure of the code in a computer program are known as...",
        true="Syntax",
        false=["Semantics", "Interpreter", "Compiler"],
        explanation="The rules that determine the correct structure of the code in a computer program are known as syntax.",
        learn_more_url="https://en.wikipedia.org/wiki/Syntax_(programming_languages)",
        difficulty=1
        ),
        QuizQuestion(
        question="The set of instructions that specifies a computation in known as...",
        true="Program",
        false=["Syntax", "Recursion", "API"],
        explanation="The set of instructions that specifies a computation in known as...",
        learn_more_url="https://www.freecodecamp.org/news/what-is-programming/",
        difficulty=1
        ),
        QuizQuestion(
        question="Each one of the alternative sequence of statements in a conditional statement is known as...",
        true="Branch",
        false=["Decision", "Path", "Loop"],
        explanation="Each one of the alternative sequence of statements in a conditional statement is known as a branch.",
        learn_more_url="https://www.freecodecamp.org/news/python-if-else-statement-conditional-statements-explained/",
        difficulty=1
        )
    ]

    css_questions = [
    
        QuizQuestion(
        question="What is RGB?",
        true="A color model",
        false=["An Internet Protocol", "HTML syntax", "A secret password"],
        explanation="RGB is an acronym that stands for {b}red{/b} {b}green{/b} {b}blue{/b}. It expresses colors in terms of the amount of red, green, and blue they are made up of and uses a human counting system with integers ranging from 0-255 or a percentage ranging from (0% - 100%).",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What color would rgb(255,0,0) give?",
        true="Red",
        false=["Green", "Blue", "Yellow"],
        explanation="Each parameter defines the intensity of each color, rgb(red, green, and blue), with an integer number ranging from 0-255. The minimum value of 0 represents that none of the color is being shown, so it is at its darkest. On the other hand, the maximum value of 255 represents that the full amount of color and the full intensity is on display",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What do R, G, and B in RGB stand for?",
        true="Red, green, and blue",
        false=["Red, gray, and black ", "Red, green, and black", "Red, gray, and blue"],
        explanation="RGB is an acronym that stands for {b}red{/b} {b}green{/b} {b}blue{/b}",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What color would rgb(255,255,255) give?",
        true="White",
        false=["Red", "Black", "Blue"],
        explanation="The maximum value of 255 represents that the full amount of all colors and their full intensity is on display.",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the role of media queries in CSS?",
        true="They help create responsive websites",
        false=["They create links to other webpages", "They add interactivity to a static webpage", "They change the font of text"],
        explanation="{b}CSS media queries{/b} allow you to create responsive websites across all screen sizes, ranging from desktop to mobile",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-media-queries-by-building-projects/",
        difficulty=1
        ),
        QuizQuestion(
        question="What are the conditions that decide if a media rule is applied?",
        true="Breakpoints",
        false=["Breaks", "Points", "Keys"],
        explanation="A breakpoint is a key to determine when to change the layout and adapt the new rules inside the media queries",
        learn_more_url="https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you change the background-image of an element in CSS?",
        true="background-image: url(\"path_to_image\");",
        false=["background-img: url(\"path_to_image\");", "background_image: url(\"path_to_image\");", "background-image: (\"path_to_image\")"],
        explanation="The background-image CSS property allows you to place an image behind any HTML element you wish. Immediately after the property you add a colon. Then, url() is used to tell CSS where the image is located. Inside the parentheses the path to the image is listed in opening and closing double quotes. This lets the browser know what URL to pull. Lastly, don't forget the semicolon to end the statement!",
        learn_more_url="https://www.freecodecamp.org/news/css-background-image-with-html-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you create a flexbox container in CSS?",
        true="display:flex;",
        false=["display:flexbox;", "display:flexcontainer;", "display:flexB;"],
        explanation="You can apply flexbox to an HTML container by using display:flex;",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set the flex container to arrange the items in a column?",
        true="flex-direction: column;",
        false=["flex-direction: row;", "flex-column: column;", "flex-direction: set-column;"],
        explanation="In CSS, you can apply flex-direction: column; to the container whose items you want arrange in a column",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set the flex container to reverse the items in a row?",
        true="flex-direction: row-reverse;",
        false=["flex-direction: reverse-row;", "flex-row: row-reverse;", "flex-direction: set-row-reverse;"],
        explanation="In CSS, you can apply flex-direction: row-reverse; to the container whose items you want to display in a row, with their order reversed.",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set the flex container to reverse the items in a column?",
        true="flex-direction: column-reverse;",
        false=["flex-direction: reverse-c;", "flex-direction: column-r;", "flex-direction: column-rev;"],
        explanation="In CSS, you can apply flex-direction: column-reverse; to the container whose items you want to display in a column, with their order reversed.",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does justify-content do in flexbox?",
        true="aligns the items along the main axis",
        false=["aligns the items to right of the y axis", "aligns the items to the left of  the x and y axis", "aligns the items to the right of the x axis"],
        explanation="In flexbox, justify-content is used to align the items in the container along the main axis",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT used with justify-content?",
        true="flex-middle",
        false=["flex-start", "flex-end", "space-around"],
        explanation="In flexbox, some of the options for justify-content include space-around, flex-end, flex-start and space-between",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does align-items do in flexbox?",
        true="aligns the items along the cross axis",
        false=["aligns the items to the right of the y axis", "aligns the items to the right of the x axis", "aligns the items to the right of the z axis"],
        explanation="In flexbox, align-items aligns the items along the cross axis",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT used with align-items?",
        true="align-middle",
        false=["flex-end", "flex-start", "baseline"],
        explanation="In flexbox, some of the options for align-items include flex-start, flex-end, baseline and stretch",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does align-self do in flexbox?",
        true="adjusts the alignment for an element",
        false=["adjust the alignment for all elements", "adjusts the alignment for hr elements", "adjusts the alignment for an img element"],
        explanation="In flexbox, align-self adjusts the alignment for an element",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you allow items to move to a new line in flexbox?",
        true="flex-wrap: wrap;",
        false=["flex: wrap;", "flex-wrap: wrap-items;", "flex-wrap: item-wrap;"],
        explanation="In flexbox, flex-wrap: wrap; will tell the computer to move items to a new line if there is not enough space",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT used with align-content?",
        true="align-bottom",
        false=["center", "space-around", "stretch"],
        explanation="In flexbox, some of the options for align-content include center, stretch, space-around and space-between",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the default position property in CSS?",
        true="position: static;",
        false=["position: relative;", "position: top;", "position: absolute;"],
        explanation="The default property in CSS is position: static; which means it follows the order of the HTML",
        learn_more_url="https://www.freecodecamp.org/news/css-positioning-position-absolute-and-relative/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you change the background color in CSS?",
        true="background-color: pink;",
        false=["bg-color: pink;", "backgroundColor: pink;", "b-color: pink;"],
        explanation="You can use the background property in CSS to change the background color of an element",
        learn_more_url="https://www.freecodecamp.org/news/css-background-color-how-to-change-the-background-color-in-html/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the rule that will override CSS style for an element?",
        true="!important",
        false=["!override", "!change", "!specific"],
        explanation="The !important rule will override the other CSS style rules for that element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you make all of the text for an element uppercase?",
        true="text-transform: uppercase;",
        false=["text-transform: toUpper;", "text-transform: upper;", "text-transform: set-upper;"],
        explanation="You can use the text-transform: uppercase; to make all of the text for that element uppercase",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you make the text for an element all lowercase?",
        true="text-transform: lowercase;",
        false=["text-transform: lower;", "text-transform: to-lower;", "text-transform: set-lower;"],
        explanation="You can use the text-transform: lowercase; to make all of the text for that element lowercase",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add content before an element?",
        true="::before",
        false=["::add-content", "::before-content", "::after"],
        explanation="You can use the ::before selector to add content before an element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add content after an element?",
        true="::after",
        false=["::after-content", "::add", "::before"],
        explanation="You can use the ::after selector to add content after an element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add a smooth scroll to the html element?",
        true="scroll-behavior: smooth;",
        false=["scroll-behavior: smooth-scroll;", "scroll: smooth;", "behavior: smooth;"],
        explanation="You can use scroll-behavior: smooth; to add a smooth scroll to the html element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="The amount of space between an element's content and its border is known as...",
        true="Padding",
        false=["Margin", "White Space", "Indentation"],
        explanation="The padding is the amount of space between the element's content and its border.",
        learn_more_url="https://www.freecodecamp.org/news/css-margins/",
        difficulty=1
        ),
        QuizQuestion(
        question="The amount of space between an element's border and its surrounding elements is known as...",
        true="Margin",
        false=["Padding", "White Space", "Indentation"],
        explanation="The margin is the amount of space between an element's border and its surrounding elements.",
        learn_more_url="https://www.freecodecamp.org/news/css-margins/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you make an image circular or oval?",
        true="border-radius: 50%;",
        false=["border-radius: 10%;", "border-radius: 0;", "border-radius: 3px;"],
        explanation="You can use the CSS property border-radius with a value of 50% to make an image circular or oval.",
        learn_more_url="https://forum.freecodecamp.org/t/freecodecamp-challenge-guide-make-circular-images-with-a-border-radius/18229",
        difficulty=1
        ),
        QuizQuestion(
        question="What CSS selector would you use to select all elements with the class blue-text?",
        true=".blue-text",
        false=["#blue-text", "a[blue-text]", "blue-text"],
        explanation="In CSS, you can select all the elements with a given class with a dot before its name.",
        learn_more_url="https://www.freecodecamp.org/news/use-css-selectors-to-style-webpage/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does CSS stand for?",
        true="Cascading Style Sheets",
        false=["Complex Style Sheets", "Complete Synchronizes Sheets", "Community Stylish System"],
        explanation="CSS stands for Cascading Style Sheets",
        learn_more_url="https://www.freecodecamp.org/news/best-css-and-css3-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the A in RGBA stand for?",
        true="Alpha",
        false=["Alphabetical", "Ambiguous", "Ancient"],
        explanation="The A in RGBA stands for Alpha. This value represents the transparency of the color.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgba()",
        difficulty=1
        ),
        QuizQuestion(
        question="Type of CSS unit that is relative to another length value.",
        true="Relative",
        false=["Absolute", "Fixed", "Dynamic"],
        explanation="In CSS, relative units are relative to other length values. Several of the relative units depend on the viweport size.",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/#why-learn-css-relative-units",
        difficulty=1
        ),
        QuizQuestion(
        question="Type of CSS unit that is tied to physical units of length. ",
        true="Absolute",
        false=["Relative", "Fixed", "Dynamic"],
        explanation="In CSS, absolute units are tied to physical units of length. ",
        learn_more_url="https://www.freecodecamp.org/news/css-unit-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you abbreviate the following Hex code? #FF0000",
        true="#F00",
        false=["#0F0", "#00F", "#0FF0"],
        explanation="To abbreviate a Hex code in CSS, include one digit of each pair of digits in the code. ",
        learn_more_url="https://www.freecodecamp.org/news/how-hex-code-colors-work-how-to-choose-colors-without-a-color-picker/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the main purpose of CSS in a website?",
        true="Style",
        false=["Structure", "Functionality", "Sound"],
        explanation="CSS is used to define the style of the elements in a website.",
        learn_more_url="https://www.freecodecamp.org/news/best-css-and-css3-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does list-style-type: circle; do in CSS?",
        true="applies circles to all of the list items in an unordered list",
        false=["applies discs to all of the list items in an unordered list", "applies decimals to all of the list items in an unordered list", "applies squares to all of the list items in an unordered list"],
        explanation="list-style-type: circle; will apply circles to all of the list items for the unordered list",
        learn_more_url="https://www.freecodecamp.org/news/html-bullet-points-how-to-create-an-unordered-list-with-the-ul-tag-example/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values does NOT apply to the CSS all shorthand property?",
        true="position",
        false=["unset", "initial", "revert"],
        explanation="The all CSS shorthand property can accept the following values: initial, inherit, unset, revert",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/CSS/all",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-name property do in CSS?",
        true="a name used to describe the animation applied to the element",
        false=["sets the duration for the animation", "sets a delay for the animation to start", "sets how many times an animation should run"],
        explanation="The animation-name is used to describe the animation applied to the element",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-duration property do in CSS?",
        true="determines how long an animation should last in seconds",
        false=["is used to style the element after the animation ends", "sets the direction for the element", "pauses the animation if the animation is running"],
        explanation="The animation-duration is used to determine how long an animation should last in seconds",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-timing-function do in CSS?",
        true="determines when the animation should speed up or slow down",
        false=["sets the direction for the element", "is used to style the element after the animation ends", "a name used to describe the animation applied to the element"],
        explanation="The animation-timing-function  is used to determine when the animation should speed up or slow down",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-delay  do in CSS?",
        true="sets a delay for the animation to start",
        false=["determines how long an animation should last in seconds", "pauses the animation if the animation is running", "determines when the animation should speed up or slow down"],
        explanation="The animation-delay is used to set a delay for the animation to start",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-iteration-count do in CSS?",
        true="sets how many times an animation should run",
        false=["a name used to describe the animation applied to the element", "determines how long an animation should last in seconds", "sets a delay for the animation to start"],
        explanation="The animation-iteration-count sets how many times the animation should run",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-direction  do in CSS?",
        true="sets the direction for the animation",
        false=["sets how many times an animation should run", "is used to style the element after the animation ends", "pauses the animation if the animation is running"],
        explanation="The animation-direction sets the direction for the animation",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-fill-mode do in the CSS?",
        true="is used to style the element after the animation ends",
        false=["sets a delay for the animation to start", "sets how many times an animation should run", "determines how long an animation should last in seconds"],
        explanation="The animation-fill-mode is used to style the element after the animation ends",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-play-state do in CSS?",
        true="is used to pause the animation if set to paused",
        false=["determines how long an animation should last in seconds", "is used to style the element after the animation ends", "sets the direction for the animation"],
        explanation="The animation-play-state is used to pause the animation if set to paused",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is an at-rule in CSS?",
        true="rules that dictate what the CSS will look like based on certain conditions",
        false=["rules to dictate how to format the HTML", "rules to dictate javascript functions", "rules to that only apply to how p elements are styled"],
        explanation="An at-rule in CSS will dictate what the CSS will look like based on certain conditions",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a media type in CSS?",
        true="the category of media for the device",
        false=["set of rules only applied to mobile devices", "category only for print media", "category only for speech"],
        explanation="A media type refers to the category of media for the device",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the all media type in CSS?",
        true="works for all devices",
        false=["only works for mobile devices", "only works for print media", "only works for tablets"],
        explanation="The all media type will work for all media devices",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the print media type in CSS?",
        true="works for devices where the media is in print preview mode",
        false=["a type of media only for 4k monitors", "a type of media that only works for desktop computers", "set of rules only applied to mobile devices"],
        explanation="The print media type works for devices where the media is in print preview mode",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the screen media type in CSS?",
        true="works for devices with screens",
        false=["works for media in print preview mode", "works for devices without screens", "only works for tablets"],
        explanation="The screen media type works for devices with screens",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the speech media type in CSS?",
        true="works for devices like screen readers where the content is read out loud to the user",
        false=["works for devices with screens", "works for devices where the media is in print preview mode", "only works for mobile devices"],
        explanation="The speech media type works for devices like screen readers where the content is read out loud to the user",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="How is the and operator used in a media query?",
        true="join multiple media features",
        false=["reverses a true query into a false", "separate multiple media features by commas", "splits media queries into separate ones"],
        explanation="The and operator is used to join multiple media features in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="How is the not operator used in a media query?",
        true="reverses a true query into a false and a false query into a true",
        false=["join multiple media features", "splits media queries into separate ones", "separate multiple media features by commas"],
        explanation="The not operator is used to reverse a true query into a false and a false query into a true",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="How is the comma operator used in a media query?",
        true="separates multiple media features by commas and apply the styles inside the curly brace if one of the conditions is true",
        false=["reverses a true query into a false and a false query into a true", "join multiple media features", "splits media queries into separate ones"],
        explanation="The comma operator is used to separate multiple media features by commas and apply the styles inside the curly brace if one of the conditions is true",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for mobile devices in a media query?",
        true="320px - 480px",
        false=["1000px - 5000px", "100px - 150px", "200px - 4000px"],
        explanation="The range of 320px — 480px can be used to target mobile devices in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for tablet devices in a media query?",
        true="481px - 768px",
        false=["300px - 7000px", "2px - 68px", "81px - 700px"],
        explanation="The range of 481px - 768px can be used to target table devices in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for laptop devices in a media query?",
        true="769px -1024px",
        false=["7px -10px", "69px -124px", "769px -10,024px"],
        explanation="The range of 769px -1024px can be used to target laptop devices ina media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for desktop and larger screens in a media query?",
        true="1025px - 1200px",
        false=["25px - 120px", "125px - 12,000px", "5px - 12px"],
        explanation="The range of 1025px - 1200px can be used to target desktop and larger screen  in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the CSS property that sets the opacity for an HTML element",
        true="opacity",
        false=["margin", "padding", "border"],
        explanation="The opacity property is used to set the opacity for an HTML element",
        learn_more_url="https://www.freecodecamp.org/news/transparent-background-image-opacity-in-css-and-html/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the code used to create a CSS grid container?",
        true="display: grid;",
        false=["display: flex;", "display: grid-box;", "display: grid-container;"],
        explanation="You can use display: grid; to create a new CSS grid container",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of grid property used to set the number and width of columns?",
        true="grid-template-columns",
        false=["grid-columns", "flex-template-columns", "template-columns-grid"],
        explanation="The grid-template-columns property is used to set the number and width for the columns",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the function to set the width for all columns in CSS grid?",
        true="repeat",
        false=["set-width", "width-all", "width-container"],
        explanation="The repeat() function is used to set the width for all of the columns in in the grid container",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What does fr stand for in CSS grid?",
        true="fraction unit",
        false=["font units", "flex unit", "fit unit"],
        explanation="fr stands for fraction unit in CSS grid",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to set the number and height for the rows?",
        true="grid-template-rows",
        false=["grid-template-columns", "grid-rows", "grid-unit-rows"],
        explanation="The grid-template-rows property is used to set the number and height for the rows",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to set the space for grid cells in rows and columns?",
        true="grid-template-areas",
        false=["grid-template-rows", "fraction unit", "repeat"],
        explanation="The grid-template-areas property is used to set the space for grid cells in rows and columns",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to create gaps between columns?",
        true="column-gap",
        false=["set-width", "fit unit", "grid-template-columns"],
        explanation="The column-gap property is used to create gaps between columns",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to create gaps between rows?",
        true="row-gap",
        false=["grid-template-rows", "grid-columns", "repeat"],
        explanation="The row-gap property is used to create gaps between rows",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to position items inside the container along the main axis?",
        true="justify-items",
        false=["justify-content", "justify-rows", "justify-columns"],
        explanation="The justify-items property is used to position items within a grid container along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is NOT a value used for the justify-items property?",
        true="gap",
        false=["start", "end", "stretch"],
        explanation="The four values that can be used for the justify-items property are start, end, center, and stretch",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position items inside the container along the y-axis?",
        true="align-items",
        false=["grid-columns", "grid-template-columns", "fraction unit"],
        explanation="The align-items property is used to position items in the container along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position the grid inside the container along the x-axis?",
        true="justify-content",
        false=["grid-template-areas", "grid-template-rows", "row-gap"],
        explanation="The justify-content property is used to position the grid in the container along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is NOT a value used for the justify-content property?",
        true="repeat",
        false=["space-around", "space-between", "space-evenly"],
        explanation="The justify-content property can accept seven values including space-around, space-between, start and end",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position the grid inside the container along the y-axis?",
        true="align-content",
        false=["justify-content", "end", "grid-unit-rows"],
        explanation="The align-content property is used to position the grid in the container along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is NOT a value used for the align-content property?",
        true="row-gap",
        false=["space-between", "center", "start"],
        explanation="The align-content property can accept seven values including space-around, space-between, start and end",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position one grid item in a container along the x-axis?",
        true="justify-self",
        false=["align-content", "grid-template-areas", "justify-rows"],
        explanation="The justify-self property is used to position one grid item in a container along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position one grid item in a container along the y-axis?",
        true="align-self",
        false=["grid-columns", "space-around", "grid-template-columns"],
        explanation="The align-self property is used to position one grid item in a container along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to adjust the size for a background image in CSS?",
        true="background-size",
        false=["background-repeat", "background-origin", "background-position"],
        explanation="The background-size property is used to adjust the size for a background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to repeat a background image?",
        true="background-repeat",
        false=["background-position-x", "background-position-y", "background-origin"],
        explanation="The background-repeat property is used to repeat the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-repeat property?",
        true="repeat-z-axis",
        false=["no-repeat", "repeat", "repeat-x"],
        explanation="The background-repeat property can take in seven values include no-repeat, repeat, repeat-x and repeat-y",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the repeat-x value do in the background-repeat property?",
        true="repeats the image along the x-axis",
        false=["repeats the image along the y-axis", "repeats the image along the z-axis", "repeats the image along both of the x-axis and y-axis"],
        explanation="The repeat-x value repeats the image along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the repeat-y value do in the background-repeat property?",
        true="repeats the image along the y-axis",
        false=["repeats the image along the x-axis", "repeats the image along both of the x-axis and y-axis", "repeats the image along the z-axis"],
        explanation="The repeat-y value repeats the image along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the no-repeat value do in the background-repeat property?",
        true="sets no repetition for the background image",
        false=["repeats the image along the z-axis", "repeats the image along the y-axis", "repeats the image along the x-axis"],
        explanation="The no-repeat value sets no repetition for the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the value that evenly distributes space in the background-repeat property?",
        true="space",
        false=["repeat", "no-repeat", "repeat-x"],
        explanation="The space value is used to evenly distributes the space in the background-repeat property",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the value that stretches the repeated images in the background-repeat property?",
        true="round",
        false=["space", "around", "rounding"],
        explanation="The round value is used to stretch the repeated images in the background-repeat property",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to change the position of the background image?",
        true="background-position",
        false=["background-clip", "background-color", "background-origin"],
        explanation="The background-position is used to change the position of the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-position property?",
        true="side-left",
        false=["top", "bottom", "right"],
        explanation="The background-position property can take in many values including of top, right, left and bottom",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to change the origin of the background image?",
        true="background-origin",
        false=["background-position", "background-clip", "background-color"],
        explanation="The background-origin property is used to set the origin for the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-origin property?",
        true="box-sizing",
        false=["border-box", "padding-box", "content-box"],
        explanation="The background-origin property can use following value border-box, padding-box, inherit, content-box",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property that clips the background image to inside the container?",
        true="background-clip",
        false=["background-color", "background-position", "background-size"],
        explanation="The background-clip property is used to clip the background image to inside the container",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property that determines if the background image is in a scroll or fixed position?",
        true="background-attachment",
        false=["background-origin", "background-clip", "background-position"],
        explanation="The background-attachment property is used to determine if the background image is in a scroll or fixed position",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-attachment property?",
        true="inherit",
        false=["local", "scroll", "fixed"],
        explanation="The background-attachment property can take in the fixed, scroll and local values",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT an example of a relative unit in CSS?",
        true="px",
        false=["rem", "em", "vh"],
        explanation="Relative units in CSS include rem, em, vh, and vw",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many pixels are equivalent to 1 rem unit?",
        true="16",
        false=["32", "12", "6"],
        explanation="One rem unit is equivalent to 16 pixels",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the relative unit that based on the root element's font size?",
        true="rem",
        false=["em", "px", "vw"],
        explanation="The rem unit is based off of the root element's font size",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the relative unit that is based its parent's font size",
        true="em",
        false=["rem", "vh", "vw"],
        explanation="The em unit is based off of the parent's font size",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the vw unit stand for?",
        true="viewport width",
        false=["view width height", "viewport weight", "viewport height"],
        explanation="The vw unit stands for viewport width",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values represents 10% of the viewport width?",
        true="10vw",
        false=["10vh", "100vw", "1000vw"],
        explanation="10vw is equivalent to 10% of the viewport width",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the vh unit stand for?",
        true="viewport height",
        false=["viewport width", "view heights", "viewing height"],
        explanation="The vh unit stands for viewport height",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values represents 20% of the viewport height?",
        true="20vh",
        false=["200vh", "2vh", "2000vh"],
        explanation="20vh is equivalent to 20% of the viewport height",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What CSS property is used to customize the marker of a list item?",
        true="list-style-type",
        false=["list-style", "list-marker-type", "list-markers"],
        explanation="The list-style-type property is used to set the marker of a list item. ",
        learn_more_url="https://www.freecodecamp.org/news/how-to-style-lists-with-css/",
        difficulty=2
        ),
        QuizQuestion(
        question="What is the universal selector in CSS?",
        true="*",
        false=["#", "$", "@"],
        explanation="The asterisk * is the universal selector in CSS. It selects all elements of any type.",
        learn_more_url="https://www.freecodecamp.org/news/use-css-selectors-to-style-webpage/",
        difficulty=2
        ),
        QuizQuestion(
        question="Fonts that are generally available across most browsers and operating systems are known as...",
        true="Web safe fonts",
        false=["General fonts", "Universal fonts", "Web Fonts"],
        explanation="Web safe fonts are the fonts that are generally available across most browsers and operating systems.",
        learn_more_url="https://www.freecodecamp.org/news/web-safe-fonts/",
        difficulty=2
        )
    ]


    css_questions = [

        QuizQuestion(
        question="What is RGB?",
        true="A color model",
        false=["An Internet Protocol", "HTML syntax", "A secret password"],
        explanation="RGB is an acronym that stands for {b}red{/b} {b}green{/b} {b}blue{/b}. It expresses colors in terms of the amount of red, green, and blue they are made up of and uses a human counting system with integers ranging from 0-255 or a percentage ranging from (0% - 100%).",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What color would rgb(255,0,0) give?",
        true="Red",
        false=["Green", "Blue", "Yellow"],
        explanation="Each parameter defines the intensity of each color, rgb(red, green, and blue), with an integer number ranging from 0-255. The minimum value of 0 represents that none of the color is being shown, so it is at its darkest. On the other hand, the maximum value of 255 represents that the full amount of color and the full intensity is on display",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What do R, G, and B in RGB stand for?",
        true="Red, green, and blue",
        false=["Red, gray, and black ", "Red, green, and black", "Red, gray, and blue"],
        explanation="RGB is an acronym that stands for {b}red{/b} {b}green{/b} {b}blue{/b}",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What color would rgb(255,255,255) give?",
        true="White",
        false=["Red", "Black", "Blue"],
        explanation="The maximum value of 255 represents that the full amount of all colors and their full intensity is on display.",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the role of media queries in CSS?",
        true="They help create responsive websites",
        false=["They create links to other webpages", "They add interactivity to a static webpage", "They change the font of text"],
        explanation="{b}CSS media queries{/b} allow you to create responsive websites across all screen sizes, ranging from desktop to mobile",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-media-queries-by-building-projects/",
        difficulty=1
        ),
        QuizQuestion(
        question="What are the conditions that decide if a media rule is applied?",
        true="Breakpoints",
        false=["Breaks", "Points", "Keys"],
        explanation="A breakpoint is a key to determine when to change the layout and adapt the new rules inside the media queries",
        learn_more_url="https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you change the background-image of an element in CSS?",
        true="background-image: url(\"path_to_image\");",
        false=["background-img: url(\"path_to_image\");", "background_image: url(\"path_to_image\");", "background-image: (\"path_to_image\")"],
        explanation="The background-image CSS property allows you to place an image behind any HTML element you wish. Immediately after the property you add a colon. Then, url() is used to tell CSS where the image is located. Inside the parentheses the path to the image is listed in opening and closing double quotes. This lets the browser know what URL to pull. Lastly, don't forget the semicolon to end the statement!",
        learn_more_url="https://www.freecodecamp.org/news/css-background-image-with-html-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you create a flexbox container in CSS?",
        true="display:flex;",
        false=["display:flexbox;", "display:flexcontainer;", "display:flexB;"],
        explanation="You can apply flexbox to an HTML container by using display:flex;",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set the flex container to arrange the items in a column?",
        true="flex-direction: column;",
        false=["flex-direction: row;", "flex-column: column;", "flex-direction: set-column;"],
        explanation="In CSS, you can apply flex-direction: column; to the container whose items you want arrange in a column",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set the flex container to reverse the items in a row?",
        true="flex-direction: row-reverse;",
        false=["flex-direction: reverse-row;", "flex-row: row-reverse;", "flex-direction: set-row-reverse;"],
        explanation="In CSS, you can apply flex-direction: row-reverse; to the container whose items you want to display in a row, with their order reversed.",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set the flex container to reverse the items in a column?",
        true="flex-direction: column-reverse;",
        false=["flex-direction: reverse-c;", "flex-direction: column-r;", "flex-direction: column-rev;"],
        explanation="In CSS, you can apply flex-direction: column-reverse; to the container whose items you want to display in a column, with their order reversed.",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does justify-content do in flexbox?",
        true="aligns the items along the main axis",
        false=["aligns the items to right of the y axis", "aligns the items to the left of  the x and y axis", "aligns the items to the right of the x axis"],
        explanation="In flexbox, justify-content is used to align the items in the container along the main axis",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT used with justify-content?",
        true="flex-middle",
        false=["flex-start", "flex-end", "space-around"],
        explanation="In flexbox, some of the options for justify-content include space-around, flex-end, flex-start and space-between",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does align-items do in flexbox?",
        true="aligns the items along the cross axis",
        false=["aligns the items to the right of the y axis", "aligns the items to the right of the x axis", "aligns the items to the right of the z axis"],
        explanation="In flexbox, align-items aligns the items along the cross axis",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT used with align-items?",
        true="align-middle",
        false=["flex-end", "flex-start", "baseline"],
        explanation="In flexbox, some of the options for align-items include flex-start, flex-end, baseline and stretch",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does align-self do in flexbox?",
        true="adjusts the alignment for an element",
        false=["adjust the alignment for all elements", "adjusts the alignment for hr elements", "adjusts the alignment for an img element"],
        explanation="In flexbox, align-self adjusts the alignment for an element",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you allow items to move to a new line in flexbox?",
        true="flex-wrap: wrap;",
        false=["flex: wrap;", "flex-wrap: wrap-items;", "flex-wrap: item-wrap;"],
        explanation="In flexbox, flex-wrap: wrap; will tell the computer to move items to a new line if there is not enough space",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT used with align-content?",
        true="align-bottom",
        false=["center", "space-around", "stretch"],
        explanation="In flexbox, some of the options for align-content include center, stretch, space-around and space-between",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the default position property in CSS?",
        true="position: static;",
        false=["position: relative;", "position: top;", "position: absolute;"],
        explanation="The default property in CSS is position: static; which means it follows the order of the HTML",
        learn_more_url="https://www.freecodecamp.org/news/css-positioning-position-absolute-and-relative/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you change the background color in CSS?",
        true="background-color: pink;",
        false=["bg-color: pink;", "backgroundColor: pink;", "b-color: pink;"],
        explanation="You can use the background property in CSS to change the background color of an element",
        learn_more_url="https://www.freecodecamp.org/news/css-background-color-how-to-change-the-background-color-in-html/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the rule that will override CSS style for an element?",
        true="!important",
        false=["!override", "!change", "!specific"],
        explanation="The !important rule will override the other CSS style rules for that element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you make all of the text for an element uppercase?",
        true="text-transform: uppercase;",
        false=["text-transform: toUpper;", "text-transform: upper;", "text-transform: set-upper;"],
        explanation="You can use the text-transform: uppercase; to make all of the text for that element uppercase",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you make the text for an element all lowercase?",
        true="text-transform: lowercase;",
        false=["text-transform: lower;", "text-transform: to-lower;", "text-transform: set-lower;"],
        explanation="You can use the text-transform: lowercase; to make all of the text for that element lowercase",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add content before an element?",
        true="::before",
        false=["::add-content", "::before-content", "::after"],
        explanation="You can use the ::before selector to add content before an element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add content after an element?",
        true="::after",
        false=["::after-content", "::add", "::before"],
        explanation="You can use the ::after selector to add content after an element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add a smooth scroll to the html element?",
        true="scroll-behavior: smooth;",
        false=["scroll-behavior: smooth-scroll;", "scroll: smooth;", "behavior: smooth;"],
        explanation="You can use scroll-behavior: smooth; to add a smooth scroll to the html element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="The amount of space between an element's content and its border is known as...",
        true="Padding",
        false=["Margin", "White Space", "Indentation"],
        explanation="The padding is the amount of space between the element's content and its border.",
        learn_more_url="https://www.freecodecamp.org/news/css-margins/",
        difficulty=1
        ),
        QuizQuestion(
        question="The amount of space between an element's border and its surrounding elements is known as...",
        true="Margin",
        false=["Padding", "White Space", "Indentation"],
        explanation="The margin is the amount of space between an element's border and its surrounding elements.",
        learn_more_url="https://www.freecodecamp.org/news/css-margins/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you make an image circular or oval?",
        true="border-radius: 50%;",
        false=["border-radius: 10%;", "border-radius: 0;", "border-radius: 3px;"],
        explanation="You can use the CSS property border-radius with a value of 50% to make an image circular or oval.",
        learn_more_url="https://forum.freecodecamp.org/t/freecodecamp-challenge-guide-make-circular-images-with-a-border-radius/18229",
        difficulty=1
        ),
        QuizQuestion(
        question="What CSS selector would you use to select all elements with the class blue-text?",
        true=".blue-text",
        false=["#blue-text", "a[blue-text]", "blue-text"],
        explanation="In CSS, you can select all the elements with a given class with a dot before its name.",
        learn_more_url="https://www.freecodecamp.org/news/use-css-selectors-to-style-webpage/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does CSS stand for?",
        true="Cascading Style Sheets",
        false=["Complex Style Sheets", "Complete Synchronizes Sheets", "Community Stylish System"],
        explanation="CSS stands for Cascading Style Sheets",
        learn_more_url="https://www.freecodecamp.org/news/best-css-and-css3-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the A in RGBA stand for?",
        true="Alpha",
        false=["Alphabetical", "Ambiguous", "Ancient"],
        explanation="The A in RGBA stands for Alpha. This value represents the transparency of the color.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgba()",
        difficulty=1
        ),
        QuizQuestion(
        question="Type of CSS unit that is relative to another length value.",
        true="Relative",
        false=["Absolute", "Fixed", "Dynamic"],
        explanation="In CSS, relative units are relative to other length values. Several of the relative units depend on the viweport size.",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/#why-learn-css-relative-units",
        difficulty=1
        ),
        QuizQuestion(
        question="Type of CSS unit that is tied to physical units of length. ",
        true="Absolute",
        false=["Relative", "Fixed", "Dynamic"],
        explanation="In CSS, absolute units are tied to physical units of length. ",
        learn_more_url="https://www.freecodecamp.org/news/css-unit-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you abbreviate the following Hex code? #FF0000",
        true="#F00",
        false=["#0F0", "#00F", "#0FF0"],
        explanation="To abbreviate a Hex code in CSS, include one digit of each pair of digits in the code. ",
        learn_more_url="https://www.freecodecamp.org/news/how-hex-code-colors-work-how-to-choose-colors-without-a-color-picker/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the main purpose of CSS in a website?",
        true="Style",
        false=["Structure", "Functionality", "Sound"],
        explanation="CSS is used to define the style of the elements in a website.",
        learn_more_url="https://www.freecodecamp.org/news/best-css-and-css3-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does list-style-type: circle; do in CSS?",
        true="applies circles to all of the list items in an unordered list",
        false=["applies discs to all of the list items in an unordered list", "applies decimals to all of the list items in an unordered list", "applies squares to all of the list items in an unordered list"],
        explanation="list-style-type: circle; will apply circles to all of the list items for the unordered list",
        learn_more_url="https://www.freecodecamp.org/news/html-bullet-points-how-to-create-an-unordered-list-with-the-ul-tag-example/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values does NOT apply to the CSS all shorthand property?",
        true="position",
        false=["unset", "initial", "revert"],
        explanation="The all CSS shorthand property can accept the following values: initial, inherit, unset, revert",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/CSS/all",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-name property do in CSS?",
        true="a name used to describe the animation applied to the element",
        false=["sets the duration for the animation", "sets a delay for the animation to start", "sets how many times an animation should run"],
        explanation="The animation-name is used to describe the animation applied to the element",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-duration property do in CSS?",
        true="determines how long an animation should last in seconds",
        false=["is used to style the element after the animation ends", "sets the direction for the element", "pauses the animation if the animation is running"],
        explanation="The animation-duration is used to determine how long an animation should last in seconds",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-timing-function do in CSS?",
        true="determines when the animation should speed up or slow down",
        false=["sets the direction for the element", "is used to style the element after the animation ends", "a name used to describe the animation applied to the element"],
        explanation="The animation-timing-function  is used to determine when the animation should speed up or slow down",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-delay  do in CSS?",
        true="sets a delay for the animation to start",
        false=["determines how long an animation should last in seconds", "pauses the animation if the animation is running", "determines when the animation should speed up or slow down"],
        explanation="The animation-delay is used to set a delay for the animation to start",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-iteration-count do in CSS?",
        true="sets how many times an animation should run",
        false=["a name used to describe the animation applied to the element", "determines how long an animation should last in seconds", "sets a delay for the animation to start"],
        explanation="The animation-iteration-count sets how many times the animation should run",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-direction  do in CSS?",
        true="sets the direction for the animation",
        false=["sets how many times an animation should run", "is used to style the element after the animation ends", "pauses the animation if the animation is running"],
        explanation="The animation-direction sets the direction for the animation",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-fill-mode do in the CSS?",
        true="is used to style the element after the animation ends",
        false=["sets a delay for the animation to start", "sets how many times an animation should run", "determines how long an animation should last in seconds"],
        explanation="The animation-fill-mode is used to style the element after the animation ends",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-play-state do in CSS?",
        true="is used to pause the animation if set to paused",
        false=["determines how long an animation should last in seconds", "is used to style the element after the animation ends", "sets the direction for the animation"],
        explanation="The animation-play-state is used to pause the animation if set to paused",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is an at-rule in CSS?",
        true="rules that dictate what the CSS will look like based on certain conditions",
        false=["rules to dictate how to format the HTML", "rules to dictate javascript functions", "rules to that only apply to how p elements are styled"],
        explanation="An at-rule in CSS will dictate what the CSS will look like based on certain conditions",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a media type in CSS?",
        true="the category of media for the device",
        false=["set of rules only applied to mobile devices", "category only for print media", "category only for speech"],
        explanation="A media type refers to the category of media for the device",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the all media type in CSS?",
        true="works for all devices",
        false=["only works for mobile devices", "only works for print media", "only works for tablets"],
        explanation="The all media type will work for all media devices",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the print media type in CSS?",
        true="works for devices where the media is in print preview mode",
        false=["a type of media only for 4k monitors", "a type of media that only works for desktop computers", "set of rules only applied to mobile devices"],
        explanation="The print media type works for devices where the media is in print preview mode",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the screen media type in CSS?",
        true="works for devices with screens",
        false=["works for media in print preview mode", "works for devices without screens", "only works for tablets"],
        explanation="The screen media type works for devices with screens",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the speech media type in CSS?",
        true="works for devices like screen readers where the content is read out loud to the user",
        false=["works for devices with screens", "works for devices where the media is in print preview mode", "only works for mobile devices"],
        explanation="The speech media type works for devices like screen readers where the content is read out loud to the user",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="How is the and operator used in a media query?",
        true="join multiple media features",
        false=["reverses a true query into a false", "separate multiple media features by commas", "splits media queries into separate ones"],
        explanation="The and operator is used to join multiple media features in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="How is the not operator used in a media query?",
        true="reverses a true query into a false and a false query into a true",
        false=["join multiple media features", "splits media queries into separate ones", "separate multiple media features by commas"],
        explanation="The not operator is used to reverse a true query into a false and a false query into a true",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="How is the comma operator used in a media query?",
        true="separates multiple media features by commas and apply the styles inside the curly brace if one of the conditions is true",
        false=["reverses a true query into a false and a false query into a true", "join multiple media features", "splits media queries into separate ones"],
        explanation="The comma operator is used to separate multiple media features by commas and apply the styles inside the curly brace if one of the conditions is true",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for mobile devices in a media query?",
        true="320px - 480px",
        false=["1000px - 5000px", "100px - 150px", "200px - 4000px"],
        explanation="The range of 320px — 480px can be used to target mobile devices in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for tablet devices in a media query?",
        true="481px - 768px",
        false=["300px - 7000px", "2px - 68px", "81px - 700px"],
        explanation="The range of 481px - 768px can be used to target table devices in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for laptop devices in a media query?",
        true="769px -1024px",
        false=["7px -10px", "69px -124px", "769px -10,024px"],
        explanation="The range of 769px -1024px can be used to target laptop devices ina media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for desktop and larger screens in a media query?",
        true="1025px - 1200px",
        false=["25px - 120px", "125px - 12,000px", "5px - 12px"],
        explanation="The range of 1025px - 1200px can be used to target desktop and larger screen  in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the CSS property that sets the opacity for an HTML element",
        true="opacity",
        false=["margin", "padding", "border"],
        explanation="The opacity property is used to set the opacity for an HTML element",
        learn_more_url="https://www.freecodecamp.org/news/transparent-background-image-opacity-in-css-and-html/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the code used to create a CSS grid container?",
        true="display: grid;",
        false=["display: flex;", "display: grid-box;", "display: grid-container;"],
        explanation="You can use display: grid; to create a new CSS grid container",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of grid property used to set the number and width of columns?",
        true="grid-template-columns",
        false=["grid-columns", "flex-template-columns", "template-columns-grid"],
        explanation="The grid-template-columns property is used to set the number and width for the columns",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the function to set the width for all columns in CSS grid?",
        true="repeat",
        false=["set-width", "width-all", "width-container"],
        explanation="The repeat() function is used to set the width for all of the columns in in the grid container",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What does fr stand for in CSS grid?",
        true="fraction unit",
        false=["font units", "flex unit", "fit unit"],
        explanation="fr stands for fraction unit in CSS grid",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to set the number and height for the rows?",
        true="grid-template-rows",
        false=["grid-template-columns", "grid-rows", "grid-unit-rows"],
        explanation="The grid-template-rows property is used to set the number and height for the rows",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to set the space for grid cells in rows and columns?",
        true="grid-template-areas",
        false=["grid-template-rows", "fraction unit", "repeat"],
        explanation="The grid-template-areas property is used to set the space for grid cells in rows and columns",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to create gaps between columns?",
        true="column-gap",
        false=["set-width", "fit unit", "grid-template-columns"],
        explanation="The column-gap property is used to create gaps between columns",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to create gaps between rows?",
        true="row-gap",
        false=["grid-template-rows", "grid-columns", "repeat"],
        explanation="The row-gap property is used to create gaps between rows",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to position items inside the container along the main axis?",
        true="justify-items",
        false=["justify-content", "justify-rows", "justify-columns"],
        explanation="The justify-items property is used to position items within a grid container along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is NOT a value used for the justify-items property?",
        true="gap",
        false=["start", "end", "stretch"],
        explanation="The four values that can be used for the justify-items property are start, end, center, and stretch",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position items inside the container along the y-axis?",
        true="align-items",
        false=["grid-columns", "grid-template-columns", "fraction unit"],
        explanation="The align-items property is used to position items in the container along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position the grid inside the container along the x-axis?",
        true="justify-content",
        false=["grid-template-areas", "grid-template-rows", "row-gap"],
        explanation="The justify-content property is used to position the grid in the container along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is NOT a value used for the justify-content property?",
        true="repeat",
        false=["space-around", "space-between", "space-evenly"],
        explanation="The justify-content property can accept seven values including space-around, space-between, start and end",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position the grid inside the container along the y-axis?",
        true="align-content",
        false=["justify-content", "end", "grid-unit-rows"],
        explanation="The align-content property is used to position the grid in the container along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is NOT a value used for the align-content property?",
        true="row-gap",
        false=["space-between", "center", "start"],
        explanation="The align-content property can accept seven values including space-around, space-between, start and end",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position one grid item in a container along the x-axis?",
        true="justify-self",
        false=["align-content", "grid-template-areas", "justify-rows"],
        explanation="The justify-self property is used to position one grid item in a container along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position one grid item in a container along the y-axis?",
        true="align-self",
        false=["grid-columns", "space-around", "grid-template-columns"],
        explanation="The align-self property is used to position one grid item in a container along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to adjust the size for a background image in CSS?",
        true="background-size",
        false=["background-repeat", "background-origin", "background-position"],
        explanation="The background-size property is used to adjust the size for a background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to repeat a background image?",
        true="background-repeat",
        false=["background-position-x", "background-position-y", "background-origin"],
        explanation="The background-repeat property is used to repeat the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-repeat property?",
        true="repeat-z-axis",
        false=["no-repeat", "repeat", "repeat-x"],
        explanation="The background-repeat property can take in seven values include no-repeat, repeat, repeat-x and repeat-y",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the repeat-x value do in the background-repeat property?",
        true="repeats the image along the x-axis",
        false=["repeats the image along the y-axis", "repeats the image along the z-axis", "repeats the image along both of the x-axis and y-axis"],
        explanation="The repeat-x value repeats the image along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the repeat-y value do in the background-repeat property?",
        true="repeats the image along the y-axis",
        false=["repeats the image along the x-axis", "repeats the image along both of the x-axis and y-axis", "repeats the image along the z-axis"],
        explanation="The repeat-y value repeats the image along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the no-repeat value do in the background-repeat property?",
        true="sets no repetition for the background image",
        false=["repeats the image along the z-axis", "repeats the image along the y-axis", "repeats the image along the x-axis"],
        explanation="The no-repeat value sets no repetition for the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the value that evenly distributes space in the background-repeat property?",
        true="space",
        false=["repeat", "no-repeat", "repeat-x"],
        explanation="The space value is used to evenly distributes the space in the background-repeat property",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the value that stretches the repeated images in the background-repeat property?",
        true="round",
        false=["space", "around", "rounding"],
        explanation="The round value is used to stretch the repeated images in the background-repeat property",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to change the position of the background image?",
        true="background-position",
        false=["background-clip", "background-color", "background-origin"],
        explanation="The background-position is used to change the position of the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-position property?",
        true="side-left",
        false=["top", "bottom", "right"],
        explanation="The background-position property can take in many values including of top, right, left and bottom",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to change the origin of the background image?",
        true="background-origin",
        false=["background-position", "background-clip", "background-color"],
        explanation="The background-origin property is used to set the origin for the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-origin property?",
        true="box-sizing",
        false=["border-box", "padding-box", "content-box"],
        explanation="The background-origin property can use following value border-box, padding-box, inherit, content-box",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property that clips the background image to inside the container?",
        true="background-clip",
        false=["background-color", "background-position", "background-size"],
        explanation="The background-clip property is used to clip the background image to inside the container",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property that determines if the background image is in a scroll or fixed position?",
        true="background-attachment",
        false=["background-origin", "background-clip", "background-position"],
        explanation="The background-attachment property is used to determine if the background image is in a scroll or fixed position",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-attachment property?",
        true="inherit",
        false=["local", "scroll", "fixed"],
        explanation="The background-attachment property can take in the fixed, scroll and local values",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT an example of a relative unit in CSS?",
        true="px",
        false=["rem", "em", "vh"],
        explanation="Relative units in CSS include rem, em, vh, and vw",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many pixels are equivalent to 1 rem unit?",
        true="16",
        false=["32", "12", "6"],
        explanation="One rem unit is equivalent to 16 pixels",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the relative unit that based on the root element's font size?",
        true="rem",
        false=["em", "px", "vw"],
        explanation="The rem unit is based off of the root element's font size",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the relative unit that is based its parent's font size",
        true="em",
        false=["rem", "vh", "vw"],
        explanation="The em unit is based off of the parent's font size",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the vw unit stand for?",
        true="viewport width",
        false=["view width height", "viewport weight", "viewport height"],
        explanation="The vw unit stands for viewport width",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values represents 10% of the viewport width?",
        true="10vw",
        false=["10vh", "100vw", "1000vw"],
        explanation="10vw is equivalent to 10% of the viewport width",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the vh unit stand for?",
        true="viewport height",
        false=["viewport width", "view heights", "viewing height"],
        explanation="The vh unit stands for viewport height",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values represents 20% of the viewport height?",
        true="20vh",
        false=["200vh", "2vh", "2000vh"],
        explanation="20vh is equivalent to 20% of the viewport height",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What CSS property is used to customize the marker of a list item?",
        true="list-style-type",
        false=["list-style", "list-marker-type", "list-markers"],
        explanation="The list-style-type property is used to set the marker of a list item. ",
        learn_more_url="https://www.freecodecamp.org/news/how-to-style-lists-with-css/",
        difficulty=2
        ),
        QuizQuestion(
        question="What is the universal selector in CSS?",
        true="*",
        false=["#", "$", "@"],
        explanation="The asterisk * is the universal selector in CSS. It selects all elements of any type.",
        learn_more_url="https://www.freecodecamp.org/news/use-css-selectors-to-style-webpage/",
        difficulty=2
        ),
        QuizQuestion(
        question="Fonts that are generally available across most browsers and operating systems are known as...",
        true="Web safe fonts",
        false=["General fonts", "Universal fonts", "Web Fonts"],
        explanation="Web safe fonts are the fonts that are generally available across most browsers and operating systems.",
        learn_more_url="https://www.freecodecamp.org/news/web-safe-fonts/",
        difficulty=2
        )
    ]

    git_questions = [

        QuizQuestion(
        question="What is Git?",
        true="A popular type of version control system ",
        false=["A sorting algorithm", "A data type", "A non-relational database"],
        explanation="Git is an open source version control system that tracks changes to your files. ",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is GitHub?",
        true="A hosting platform for Git repositories ",
        false=["An online IDE", "A popular database", "A subscription based platform to sell coding classes"],
        explanation="GitHub is a popular hosting platform for developers to store their Git repositories and collaborate with other developers all around the world.",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you check for the version of Git installed on your machine?",
        true="git --version",
        false=["git &version", "git <version>", "git /version"],
        explanation="In the command line, you can use git --version to check which version of Git is installed on your local machine",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set your username in Git?",
        true="git config --global user.name \"YOUR_USERNAME\"",
        false=["git config --global password \"YOUR_USERNAME\"", "git config &user \"YOUR_USERNAME\"", "git create --user \"YOUR_USERNAME\""],
        explanation="In the command line, you can use git config --global user.name \"YOUR_USERNAME\"",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set your email in Git?",
        true="git config --global user.email \"YOUR_EMAIL\"",
        false=["git config --global set email address \"YOUR_EMAIL\"", "git config --email address \"YOUR_EMAIL\"", "git create user email \"YOUR_EMAIL\""],
        explanation="In the command line, you can use git config --global user.email \"YOUR_EMAIL\" to set your email address in Git",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you initialize a new Git repository?",
        true="git init",
        false=["git create new repo", "git config init repo", "git new repo"],
        explanation="In the command line, you can use git init to initialize a new Git repository",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the committed state in Git?",
        true="all of the files have been saved to the local repo and are ready to be pushed to the remote repo",
        false=["the files need to be saved to the local repo", "the files have been successfully pushed to the remote repo", "the files have been deleted from the local repo"],
        explanation="The committed state is when all of the files have been saved to the local repo and are ready to be pushed to the remote repo",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a modified state in Git?",
        true="changes have been made to the files but those changes are not saved yet",
        false=["a new local repository has been created", "a new remote repository has been created", "the files have been saved and need to be pushed to the remote repository"],
        explanation="The modified state is when changes have been made to the files but those changes are not saved yet",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a staged state in Git?",
        true="the files are ready to be committed",
        false=["the files are ready to be deleted", "a new local repository has been created", "the files need to be saved to the remote repository"],
        explanation="The staged state is when the files are ready to be committed",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add all of the files in the local repository?",
        true="git add .",
        false=["git add all files", "git add --all files", "git add <all files"],
        explanation="In the command line, you can use git add . to add all of the files in your local repository",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add a specific file in Git?",
        true="git add filename",
        false=["git add < filename", "git add *filename", "git add %filename"],
        explanation="In the command line, you can use git add filename to add a specific file",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you commit files in Git?",
        true="git commit -m \"commit message\"",
        false=["git commit --add message", "git commit < add message", "git add message"],
        explanation="In the command line, you can use git commit -m \"commit message\" to commit your changes",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the -m flag in Git?",
        true="shorthand for message",
        false=["shorthand for main", "shorthand for mistake", "shorthand for merge"],
        explanation="The -m flag in Git is shorthand for message",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you create a connection between the local repository and the remote one?",
        true="git remote add origin git-url",
        false=["git add remote and local", "git remote local", "git local remote"],
        explanation="In the command line, you can use git remote add origin git-url to connect the local repository to the remote one",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you push changes from the local repository to the remote one in Git?",
        true="git push -u origin main",
        false=["git push changes", "git push all changes", "git push --to main branch"],
        explanation="In the command line, you can use git push -u origin main to push your changes from the local repository to the remote one",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you check for the status of your working directory in Git?",
        true="git status",
        false=["git check status", "git share status", "git show status"],
        explanation="In the command line, you can use git status to check the current status of your working directory",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you switch to a new branch in Git?",
        true="git checkout branch-name",
        false=["git switch branch-name", "git switch to branch-name", "git change branch-name"],
        explanation="In the command line, you can use git checkout branch-name to switch to a different branch",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How to create a new branch and switch to it in Git?",
        true="git checkout -b new-branch-name",
        false=["git create -b new-branch-name", "git change -b new-branch-name", "git create --change -b new-branch-name"],
        explanation="In the command line, you can use git checkout -b new-branch-name to create a new branch and switch to it",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you switch back to the main branch in Git?",
        true="git checkout main",
        false=["git switch main", "git change main", "git go to main"],
        explanation="In the command line, you can use git checkout main to switch over to the main branch",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you clone a remote repository in Git?",
        true="git clone",
        false=["git copy", "git copy url", "git clone --copy"],
        explanation="In the command line, you can use git clone followed by the remote url address for the repository you want to clone into your local machine",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you integrate changes from one branch to another in Git?",
        true="git merge",
        false=["git copy into", "git merge --docs", "git clone --docs"],
        explanation="In the command line, you can use git merge to integrate changes from one branch to another",
        learn_more_url="https://www.freecodecamp.org/news/git-and-github-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you push a branch to a remote repository in Git?",
        true="git push -u <remote> <branch-name>",
        false=["git push -u <branch-name> <remote>", "git copy url", "git pull url"],
        explanation="In the command line, you can use git push -u <remote> <branch-name> to push a branch to a remote repository.",
        learn_more_url="https://www.freecodecamp.org/news/10-important-git-commands-that-every-developer-should-know/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you list all the local branches in your repository in Git?",
        true="git branch",
        false=["git list", "git ls", "git branches"],
        explanation="You can use git branch to list all the local branches in the repository. ",
        learn_more_url="https://www.freecodecamp.org/news/10-important-git-commands-that-every-developer-should-know/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you delete a branch from a repository in Git?",
        true="git branch -d <branch-name>",
        false=["git branch <branch-name>", "git delete <branch-name>", "git del <branch-name>"],
        explanation="You can use git branch -d <branch-name> to delete a branch from the repository.",
        learn_more_url="https://www.freecodecamp.org/news/10-important-git-commands-that-every-developer-should-know/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you see the current status of the current branch in Git?",
        true="git status",
        false=["git info", "git show status", "git show"],
        explanation="You can see the status of the current branch with git status in Git.",
        learn_more_url="https://www.freecodecamp.org/news/10-important-git-commands-that-every-developer-should-know/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you pull changes made to the remote repository?",
        true="git pull <remote>",
        false=["git <remote> pull", "git push <remote>", "git pul <remote>"],
        explanation="You can pull changes from the remote repository with git pull <remote>.",
        learn_more_url="https://www.freecodecamp.org/news/10-important-git-commands-that-every-developer-should-know/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you list all the commits in a local repository in reverse chronological order?",
        true="git log",
        false=["git show", "git ls", "git commits"],
        explanation="You can use git log to see the commits in a repository in reverse chronological order.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-git-learn-git-version-control/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you change the text editor used to write commit messages in Git?",
        true="git config --global core.editor <editor>",
        false=["git config email <editor>", "git set editor <editor>", "git config <editor>"],
        explanation="You can use git config --global core.editor <editor> to set the text editor that will be used to write commit messages and to work with Git in general.",
        learn_more_url="https://www.freecodecamp.org/news/best-git-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you add color to Git output?",
        true="git config --global color.ui true",
        false=["git config --global color.ui false", "git set --global color.ui true", "git config --global true"],
        explanation="You can use git config --global color.ui true to add color to Git output.",
        learn_more_url="https://www.freecodecamp.org/news/best-git-tutorial/",
        difficulty=1
        )
    ]

    html_questions = [

        QuizQuestion(
        question="What does HTML stand for?",
        true="Hyper Text Markup Language",
        false=["Hyper Text Marked Language", "Hyper Text Marked Links", "Hyper Text Machine Language"],
        explanation="HTML stands for Hyper Text Markup Language",
        learn_more_url="https://www.freecodecamp.org/news/html-crash-course/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used for creating a hyperlink?",
        true="<a>",
        false=["<hyperlink>", "<href>", "<link>"],
        explanation="You create links by using an opening <a> and closing </a> tag",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-hyperlink-definition-for-html-link-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML attribute is used when creating a hyperlink?",
        true="href",
        false=["src", "id", "style"],
        explanation="On the opening tag, <a>, an href attribute is added, which is short for hypertext reference. The value of the href attribute specifies the desired URL you want the link to take users to when the link text is clicked.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-hyperlink-definition-for-html-link-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to make text bold?",
        true="<b>",
        false=["<br>", "<bold>", "<p>"],
        explanation="The <b> tag is used to to make a portion of the text bold without carrying any special importance",
        learn_more_url="https://www.freecodecamp.org/news/html-bold-text-tutorial-how-to-use-the-b-tag/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to create an unordered(bulleted) list?",
        true="<ul>",
        false=["<ol>", "<li>", "<a>"],
        explanation=" The <ul> tag is used to create an unordered list. Within the <ul> and <ul/> tags, you use the <li> and </li> tags, to create individual list items.",
        learn_more_url="https://www.freecodecamp.org/news/html-list-how-to-use-bullet-points-ordered-and-unordered-lists/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which value of the target attribute opens a link in a new tab?",
        true="_blank",
        false=["_parent", "_self", "_top"],
        explanation="By default the browser opens links in the same tab. You add the target attribute to the opening <a> tag, and give it the value _blank which opens links in a new tab.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-hyperlink-definition-for-html-link-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a hyperlink?",
        true="A web reference to data",
        false=["A piece of computer hardware", "An executable programming script", "A website"],
        explanation="A hyperlink, also called a link or web link, contains an address for a destination and acts as a reference to data. A user can easily follow, jump to, and be directed to the destination by either clicking, tapping on, or hovering over the link.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-hyperlink-definition-for-html-link-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to italicize text?",
        true="<i>",
        false=["<b>", "<span>", "<li>"],
        explanation="The <i> tag displays text in italic",
        learn_more_url="https://www.freecodecamp.org/news/html-italics-tutorial-how-to-make-text-italic-with-the-i-tag/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you write a comment in HTML?",
        true="<!-- I am a comment! -->",
        false=["X!--I am a comment!--X", "V!--I am a comment!--V", ">!--I am a comment!--<"],
        explanation="The syntax for an HTML tag is <!-- I am a comment! -->",
        learn_more_url="https://www.freecodecamp.org/news/html-comment-how-to-comment-out-a-line-or-tag-in-html/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the nav element in HTML?",
        true="A container for navigation links",
        false=["A container for quotes", "A container for paragraph tags", "A container for headings"],
        explanation="The nav element is a semantic tag used to contain navigation links.",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the main element in HTML?",
        true="A tag used for the main content of the HTML page",
        false=["A tag used only to contain images", "A tag used to only contain links", "A tag used to only contain paragraphs"],
        explanation="The main element is a semantic tag used to contain all of the main content of the HTML page",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a section element in HTML?",
        true="A tag used to group related content into sections",
        false=["A tag used to group images", "A tag to group headings", "A tag used to group links"],
        explanation="The section element is a tag used to group related content into sections",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the header element in HTML?",
        true="A tag used to group introductory content including navigation links",
        false=["A tag used to group comment tags", "A tag used to group block quotes", "A tag used to group figure elements"],
        explanation="The header element is a tag used to group introductory content including navigation links",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the footer element in HTML?",
        true="A tag used to specify the footer of the HTML document",
        false=["A tag used to specify the header of the HTML document", "A tag used to specify a paragraph of the HTML document", "A tag used to specify the main content of the HTML document"],
        explanation="The footer element is a tag used to specify the footer of the HTML document. This element will usually contain copyright information",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is an aside element in HTML?",
        true="An HTML element typically used for sidebar information",
        false=["An HTML element typically used for footer information", "An HTML element typically used for header information", "An HTML element typically used for links"],
        explanation="An aside is an HTML element typically used for sidebar information",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the code element in HTML?",
        true="An HTML element used for displaying code snippets",
        false=["An HTML element used for displaying images", "An HTML element used for displaying links", "An HTML element used for displaying paragraphs"],
        explanation="The code element is used for displaying code snippets",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the article tag in HTML?",
        true="A tag used for content that is independent from the main content of the HTML page",
        false=["A tag used for quotes", "A tag used for code", "A tag used for links"],
        explanation="The article element is used for content that is independent from the main content of the HTML page",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the blockquote element in HTML?",
        true="A tag used to quote text from another source",
        false=["A tag used to number quotes", "A tag used to style quotes", "A tag used to turn quotes into links"],
        explanation="The blockquote element is used to quote text from another source",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the mark element in HTML?",
        true="An element used to highlight text",
        false=["A tag used to create an ordered list", "A tag used to create quotes", "A tag used to create headings"],
        explanation="The mark element is used to highlight text",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you create a button using the input tag in HTML?",
        true="<input type=\"button\" value=\"Sample Button\" />",
        false=["<input type=\"checkbox\" value=\"Sample Button\" />", "<input type=\"date\" value=\"Sample Button\" />", "<input type=\"color\" value=\"Sample Button\" />"],
        explanation="You can create a button using the input tag and set the type attribute to button",
        learn_more_url="https://www.freecodecamp.org/news/html-button-type-how-to-add-buttons-to-your-website/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you create a submit button in HTML?",
        true="<input type=\"submit\" value=\"Submit\" />",
        false=["<input type=\"number\" value=\"Submit\" />", "<input type=\"email\" value=\"Submit\" />", "<input type=\"reset\" value=\"Submit\" />"],
        explanation="You can create a submit by using the input tag and set the type attribute to submit",
        learn_more_url="https://www.freecodecamp.org/news/html-button-type-how-to-add-buttons-to-your-website/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the button tag in HTML?",
        true="A tag used to create buttons for your HTML page",
        false=["A tag used to create images", "A tag used to create quotes", "A tag used to create links"],
        explanation="The button tag is used to add buttons to your HTML page",
        learn_more_url="https://www.freecodecamp.org/news/html-button-type-how-to-add-buttons-to-your-website/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a div tag in HTML?",
        true="A generic block level container for grouping content",
        false=["A container used to only group images", "A container used to only group headings", "A container used to only group code elements"],
        explanation="The div tag is a generic container for grouping content in the HTML page",
        learn_more_url="https://www.freecodecamp.org/news/span-vs-div-html-tags-what-is-the-difference/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a span tag in HTML?",
        true="A generic inline container for grouping content",
        false=["A container used to only group footer links", "A container used to only header content", "A container used to only group navigation links"],
        explanation="A span tag is a generic inline container for grouping content in the HTML page",
        learn_more_url="https://www.freecodecamp.org/news/span-vs-div-html-tags-what-is-the-difference/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the table tag in HTML?",
        true="An element to create rows and columns of data in HTML",
        false=["An element to embed sound in an HTML document", "An element to represent side comments", "An element used for a specific set of time"],
        explanation="The table tag create rows and columns of data in HTML",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the <tr> tag in HTML?",
        true="An element that represents a row in a table",
        false=["A tag used to create buttons for your HTML page", "A container used to only group headings", "A tag used to group block quotes"],
        explanation="The <tr> tag is an element that represents a row in a table",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the <td> tag in HTML?",
        true="An element used to create data cells in a table",
        false=["A tag that represents an abbreviation", "A tag used to create word breaks", "A tag used to create a horizontal line"],
        explanation="The <td> tag is an element used to create data cells in a table",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the <th> tag in HTML?",
        true="An element used to create table headings in a table",
        false=["An element that represents a row in a table", "An element used to create data cells in a table", "A generic block level container for grouping content in a table"],
        explanation="The <th> tag is an element used to create table headings in a table",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the caption tag in an HTML table?",
        true="An element used to create captions for a table",
        false=["An element used to create images in a table", "An element used to create links in a table", "A element used to create headings in a table"],
        explanation="The caption tag is an element used to create captions for a table",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a colspan attribute in an HTML table?",
        true="Represents the number of columns a cell should span in a table",
        false=["Represents the number of rows a cell should span in a table", "Represents the number of links in a table", "Represents the number of images in a table"],
        explanation="The colspan attribute represents the number of columns a cell should span in a table",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a rowspan attribute in an HTML table?",
        true="Represents the number of rows a cell should span in a table",
        false=["Represents the number of columns a cell should span in a table", "Represents the number of headings in a table", "Represents the number of code elements in a table"],
        explanation="The rowspan attribute represents the number of rows a cell should span in a table",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which tag is used to represent the header for an HTML table?",
        true="<thead>",
        false=["<img>", "<tbody>", "<tfoot>"],
        explanation="The <thead> tag is used to represent the header of an HTML table",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which tag is used to represent the main body for an HTML table?",
        true="<tbody>",
        false=["<tmain>", "<content>", "<td>"],
        explanation="The <tbody> tag is used to represent the main content for an HTML table",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which tag is used to represent the footer for an HTML table?",
        true="<tfoot>",
        false=["<tfooter>", "<tfooting>", "<tfoots>"],
        explanation="The <tfoot> tag is used to represent the footer content for an HTML table",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the first tag you add to a HTML5 document?",
        true="The <!doctype html> tag",
        false=["The html tag", "The header tag", "The body tag"],
        explanation="The first element on every HTML page is doctype. It tells the browser to expect HTML and what version to use. For the newest version of HTML, the element should look like this: <!doctype html>",
        learn_more_url="https://www.freecodecamp.org/news/html-crash-course/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the syntax for creating a mailto link?",
        true="<a href=\"mailto:johndoe@fakeemail.com\">Example mailto link</a>",
        false=["<a name=\"mailto:johndoe@fakeemail.com\">Example mailto link</a>", "<a src=\"mailto:johndoe@fakeemail.com\">Example mailto link</a>", "<a link=\"mailto:johndoe@fakeemail.com\">Example mailto link</a>"],
        explanation="This is the correct syntax for a mailto link: <a href=\"mailto:johndoe@fakeemail.com\">Example mailto link</a>",
        learn_more_url="https://www.freecodecamp.org/news/mailto-link-how-to-make-an-html-email-link-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT an attribute for the select tag?",
        true="src",
        false=["name", "multiple", "required"],
        explanation="The select tag can have the following attributes: name, multiple,required, size, disabled and autofocus",
        learn_more_url="https://www.freecodecamp.org/news/html-select-tag-how-to-make-a-dropdown-menu-or-combo-list/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which HTML element contains the select tag?",
        true="form tag",
        false=["anchor tag", "img tag", "footer tag"],
        explanation="The select tag is nested inside the form tag so the data can be sent to the server when the form is submitted.",
        learn_more_url="https://www.freecodecamp.org/news/html-select-tag-how-to-make-a-dropdown-menu-or-combo-list/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the tag nested inside the select tag?",
        true="option tag",
        false=["h1 tag", "code tag", "aside tag"],
        explanation="The option tag is nested inside the select tag and it serves to provide options for the dropdown menu.",
        learn_more_url="https://www.freecodecamp.org/news/html-select-tag-how-to-make-a-dropdown-menu-or-combo-list/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the size attribute do in the select tag?",
        true="sets the number of options shown on default",
        false=["sets the width of the select tag", "set the height of the select tag", "sets the width and height of the select tag"],
        explanation="The size attribute sets the number of options shown on default inside the select dropdown menu",
        learn_more_url="https://www.freecodecamp.org/news/html-select-tag-how-to-make-a-dropdown-menu-or-combo-list/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the multiple attribute do in the select tag?",
        true="allows the user to choose multiple options in the select tag",
        false=["a way to add multiple select tags", "a way to add multiple option tags", "a way to add multiple link tags"],
        explanation="The multiple attribute allows the user to choose multiple options in the select tag.",
        learn_more_url="https://www.freecodecamp.org/news/html-select-tag-how-to-make-a-dropdown-menu-or-combo-list/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the optgroup element do in HTML?",
        true="groups option elements together in the select tag",
        false=["groups labels together in the select tag", "groups form tags together", "groups inputs together in the form"],
        explanation="The optgroup groups option elements together in the select tag",
        learn_more_url="https://www.freecodecamp.org/news/html-select-tag-how-to-make-a-dropdown-menu-or-combo-list/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the Doctype do in HTML?",
        true="specifies the HTML version for the document",
        false=["specifies the type of CSS used", "specifies the type of JavaScript used", "specifies the number of elements in the HTML document"],
        explanation="The Doctype is used to specify the HTML version for the document",
        learn_more_url="https://www.freecodecamp.org/news/what-is-html-definition-and-meaning/",
        difficulty=1
        ),
        QuizQuestion(
        question="What are the html tags?",
        true="root element that contains all other HTML tags",
        false=["an element that only contains all paragraph tags", "an element that only contains all image tags", "an element that only contains anchor tags"],
        explanation="The html tag is the root level element that contains all of the other HTML elements",
        learn_more_url="https://www.freecodecamp.org/news/what-is-html-definition-and-meaning/",
        difficulty=1
        ),
        QuizQuestion(
        question="What are the head tags in HTML?",
        true="a tag that contains metadata for a website",
        false=["a tag that contains table cells for a table", "a tag that contains header elements", "a tag that contains navigation links"],
        explanation="The head tags contain metadata including title and stylesheets for a website",
        learn_more_url="https://www.freecodecamp.org/news/what-is-html-definition-and-meaning/",
        difficulty=1
        ),
        QuizQuestion(
        question="What are meta tags in HTML?",
        true="defines metadata for the HTML document",
        false=["defines the number of elements in the HTML document", "defines the number of img tags in the HTML document", "defines the number of p tags in the HTML document"],
        explanation="The meta tags define metadata for the HTML document",
        learn_more_url="https://www.freecodecamp.org/news/what-is-html-definition-and-meaning/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the title tag in HTML?",
        true="defines the title for the HTML document",
        false=["defines the subtitle for the HTML document", "displays the headings for the HTML document", "displays the paragraph tags for the HTML document"],
        explanation="The title tag defines the title for the HTML document",
        learn_more_url="https://www.freecodecamp.org/news/what-is-html-definition-and-meaning/",
        difficulty=1
        ),
        QuizQuestion(
        question="What are the body tags in HTML?",
        true="defines the body content for the HTML document",
        false=["defines the header content for the HTML document", "defines the image content for the HTML document", "defines the table content for the HTML document"],
        explanation="The body tags defines the body content for the HTML document",
        learn_more_url="https://www.freecodecamp.org/news/what-is-html-definition-and-meaning/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is semantic HTML?",
        true="HTML tags that hold special meaning",
        false=["generic HTML tags that hold no meaning", "tags that only hold special meaning for links", "tags that only hold special meaning for table tags"],
        explanation="Semantic HTML tags are HTML elements that hold special meaning",
        learn_more_url="https://www.freecodecamp.org/news/what-is-html-definition-and-meaning/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the correct code for linking a CSS stylesheet to an HTML file?",
        true="<link rel=\"stylesheet\" src=\"style.css\">",
        false=["<anchor rel=\"stylesheet\" src=\"style.css\">", "<links rel=\"stylesheet\" src=\"style.css\"></links>", "<a rel=\"stylesheet\" src=\"style.css\"></a>"],
        explanation="The link tag is used to link your CSS stylesheet to your HTML file",
        learn_more_url="https://www.freecodecamp.org/news/external-css-stylesheets-how-to-link-css-to-html-and-import-into-head/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the rel attribute in the link tag?",
        true="shows the relationship between the HTML file and linked document",
        false=["defines the relationship between an img tag and p tag", "defines the relationship between a table tag and td tag", "defines the relationship between an ul tag and li tag"],
        explanation="The rel attribute is used to show the relationship between the linked document and HTML file",
        learn_more_url="https://www.freecodecamp.org/news/external-css-stylesheets-how-to-link-css-to-html-and-import-into-head/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the src attribute do in the link tag?",
        true="tells the computer where to import the document",
        false=["tells the computer where to export the document", "specifies the number of link tags in the HTML document", "specifies the number of anchor tags in the HTML document"],
        explanation="The src attribute tells the computer where to import the document",
        learn_more_url="https://www.freecodecamp.org/news/external-css-stylesheets-how-to-link-css-to-html-and-import-into-head/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the type attribute in the link tag?",
        true="describes the type of content for the linked document",
        false=["provides descriptive text for an img", "opens up the link tag in another browser window", "provides the width and height for a link tag"],
        explanation="The type attribute describes the type of content for the linked document",
        learn_more_url="https://www.freecodecamp.org/news/external-css-stylesheets-how-to-link-css-to-html-and-import-into-head/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the media attribute in the link tag?",
        true="Specifies the type of media that should be used when importing the linked content",
        false=["tells the computer to import the linked content for phones only", "tells the computer to import the linked content for laptops only", "tells the computer to import the linked content for tablets only"],
        explanation="The media attribute specifies the type of media that should be used when importing the linked content",
        learn_more_url="https://www.freecodecamp.org/news/external-css-stylesheets-how-to-link-css-to-html-and-import-into-head/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which tag is used to create line breaks in HTML?",
        true="<br>",
        false=["<img>", "<a>", "<p>"],
        explanation="The <br> tag is used to create a line break in the HTML document",
        learn_more_url="https://www.freecodecamp.org/news/html-line-break-how-to-break-a-line-with-the-html-br-tag/",
        difficulty=1
        ),
        QuizQuestion(
        question="What  makes up an element in HTML?",
        true="The opening tag, any attributes, text or other content  in between and lastly the closing tag",
        false=["Just the closing tag", "Just the closing tag and text content", "Just the opening tag"],
        explanation="The terms elements and tags are used interchangeably. Tags consist of left and right angle brackets.( < and >) and often come in pairs, with an opening and closing one. Elements have an opening tag and a closing tag, attributes that go inside the starting tag and text content (and possibly other elements) in between the opening and closing tag. So,an element refers to the whole thing.",
        learn_more_url="https://www.freecodecamp.org/news/the-html-handbook/#html-basics",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you change the font-size of an h1 tag using inline CSS?",
        true="<h1 style=\"font-size: 4rem\">freeCodeCamp</h1>",
        false=["<h1 css=\"font-size: 4rem\">freeCodeCamp</h1>", "<h1 font=\"font-size: 4rem\">freeCodeCamp</h1>", "<h1 fontSize=\"font-size: 4rem\">freeCodeCamp</h1>"],
        explanation="To change the font size of an HTML tag, you can use the style attribute and the font-size property",
        learn_more_url="https://www.freecodecamp.org/news/html-font-style-how-to-change-text-color-and-size-with-an-html-tag/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a character entity?",
        true="used to display reserved HTML characters on the page",
        false=["used to change the color for HTML characters", "used to change the font for HTML characters", "used to change the width of HTML characters"],
        explanation="Character entities allow you to display reserved HTML characters in your document.",
        learn_more_url="https://www.freecodecamp.org/news/html-space-how-to-add-a-non-breaking-space-with-the-nbsp-character-entity/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the character entity of the less than symbol in HTML?",
        true="&lt;",
        false=["&lessthan;", "&less;", "&lthan;"],
        explanation="You can use the &lt; to display a less than symbol in HTML",
        learn_more_url="https://www.freecodecamp.org/news/html-space-how-to-add-a-non-breaking-space-with-the-nbsp-character-entity/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the character entity of the greater than symbol in HTML?",
        true="&gt;",
        false=["&greaterthan;", "&greater;", "&gthan;"],
        explanation="You can use the &gt; entity to display a greater than symbol in HTML",
        learn_more_url="https://www.freecodecamp.org/news/html-space-how-to-add-a-non-breaking-space-with-the-nbsp-character-entity/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add a non-breaking space in HTML?",
        true="&nbsp;",
        false=["&breakingspace;", "&nonbreaking;", "&n-b-s-p;"],
        explanation="You can use the &nbsp; entity to display the non-breaking space in HTML",
        learn_more_url="https://www.freecodecamp.org/news/html-space-how-to-add-a-non-breaking-space-with-the-nbsp-character-entity/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add two non-breaking spaces in HTML?",
        true="&ensp;",
        false=["&twospaces;", "&e-n-s-p;", "&enspaces;"],
        explanation="You can use the &ensp; entity to display two non-breaking spaces in HTML",
        learn_more_url="https://www.freecodecamp.org/news/html-space-how-to-add-a-non-breaking-space-with-the-nbsp-character-entity/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add four non-breaking spaces in HTML?",
        true="&emsp;",
        false=["&fourspaces;", "&e-m-s-p;", "&emspaces;"],
        explanation="You can use the &emsp; entity to display four non-breaking spaces in HTML",
        learn_more_url="https://www.freecodecamp.org/news/html-space-how-to-add-a-non-breaking-space-with-the-nbsp-character-entity/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is an HTML 5 boilerplate?",
        true="block of code you use as a starter template for any HTML document",
        false=["a block on code that groups images", "a block on code that groups links", "a block of code that groups forms"],
        explanation="An HTML 5 boilerplate, is a block of code you use as a starter template for any HTML document",
        learn_more_url="https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the viewport meta tag in HTML?",
        true="renders the width of the page to the width of the device's screen size.",
        false=["sets the viewport for phones only", "sets the viewport for laptops only", "sets the viewport for 4k monitors"],
        explanation="This tag renders the width of the page to the width of the device's screen size.",
        learn_more_url="https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does X-UA-Compatible mean?",
        true="specifies the document mode for Internet Explorer.",
        false=["specifies the document mode for Google chrome", "specifies the document mode for Safari", "specifies the document mode for Brave"],
        explanation="This <meta> tag specifies the document mode for Internet Explorer.",
        learn_more_url="https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/",
        difficulty=1
        ),
        QuizQuestion(
        question="What are script tags in HTML?",
        true="used for client side JavaScript code",
        false=["used for server side JavaScript code", "used to link SQL databases", "used to link noSQL databases"],
        explanation="The script tag is used for client side JavaScript code.",
        learn_more_url="https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the <u> tag stand for?",
        true="Unarticulated Annotation element",
        false=["Unarticulated Anchor element", "Unarticulated Aside element", "Unarticulated Article element"],
        explanation="The <u> tag stands for Unarticulated Annotation element",
        learn_more_url="https://www.freecodecamp.org/news/html-underline-text-how-to-use-the-u-tag-with-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the default styling for the <u> tag?",
        true="single underline",
        false=["line through", "line above the text", "no line at all"],
        explanation="The default styling for the u tag is a single underline",
        learn_more_url="https://www.freecodecamp.org/news/html-underline-text-how-to-use-the-u-tag-with-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common use for the <u> tag?",
        true="to point out misspelled words",
        false=["to change the color for text", "to create an unordered list", "to highlight a portion of text"],
        explanation="A common use for the u tag is to point out misspelled words",
        learn_more_url="https://www.freecodecamp.org/news/html-underline-text-how-to-use-the-u-tag-with-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the attribute that allows you to set an element's tab position?",
        true="tabindex",
        false=["style", "hover", "name"],
        explanation="You can use the tabindex attribute to set an element's tab position",
        learn_more_url="https://www.freecodecamp.org/news/html-roving-tabindex-attribute-explained-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the default value for the tabindex attribute?",
        true="0",
        false=["12", "14", "7"],
        explanation="The default value for the tabindex attribute is 0",
        learn_more_url="https://www.freecodecamp.org/news/html-roving-tabindex-attribute-explained-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the range of values for the tabindex attribute?",
        true="0 to 32767",
        false=["-9 to 30", "0 to 578", "-20 to 3000"],
        explanation="The tabindex attribute accepts a range of integers from 0 to 32767",
        learn_more_url="https://www.freecodecamp.org/news/html-roving-tabindex-attribute-explained-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the <i> tag stand for?",
        true="Idiomatic Text element",
        false=["Inline Text element", "Intent Text element", "Inline Table element"],
        explanation="The <i> tag stands for Idiomatic Text element.",
        learn_more_url="https://www.freecodecamp.org/news/html-italics-tutorial-how-to-make-text-italic-with-the-i-tag/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the semantic meaning behind the <i> tag?",
        true="span of text that represents a change in mood or quality of text",
        false=["block on text used to highlight misspelled words", "span of text used to signal high importance", "block of text used to represent the main content of the HTML page"],
        explanation="The <i> tag is a span of text that represents a change in mood or quality of text",
        learn_more_url="https://www.freecodecamp.org/news/html-italics-tutorial-how-to-make-text-italic-with-the-i-tag/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which description is NOT an appropriate use for the <i> tag?",
        true="used to place emphasis on a word or span of text",
        false=["taxonomic descriptions", "to show someone's thoughts", "to mark phrases in a different language"],
        explanation="The <i> tag can be used to mark phrases in a different language, show someone's thoughts, or for taxonomic descriptions",
        learn_more_url="https://www.freecodecamp.org/news/html-italics-tutorial-how-to-make-text-italic-with-the-i-tag/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the tag that adds emphasis on a word or span of text.?",
        true="<em>",
        false=["<p>", "<i>", "<hr>"],
        explanation="The <em> tag is used to add emphasis on a word or span of text in HTML",
        learn_more_url="https://www.freecodecamp.org/news/html-italics-tutorial-how-to-make-text-italic-with-the-i-tag/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the HTML character entity for double quotes?",
        true="&quot;",
        false=["&quotes;", "&doublequot;", "&dquot;"],
        explanation="The &quot; character entity is used to display quotes in HTML",
        learn_more_url="https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the HTML character entity for the ampersand sign?",
        true="&amp;",
        false=["&amper;", "&and;", "&ampsand;"],
        explanation="The &amp; character entity is used to dispaly the ampersand sign in HTML",
        learn_more_url="https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the HTML character entity for the Euro sign?",
        true="&euro;",
        false=["&esign;", "&eurosign;", "&eu;"],
        explanation="The &euro; character entity is used to display the Euro sign in HTML",
        learn_more_url="https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the HTML character entity for the left single quote symbol?",
        true="&lsquo;",
        false=["&rsquo;", "&leftquo;", "&lsquotes;"],
        explanation="The &lsquo; character entity is used to display the left single quote symbol in HTML",
        learn_more_url="https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the HTML character entity for the right single quote symbol?",
        true="&rsquo;",
        false=["&lsquo;", "&rightquo;", "&rsquote;"],
        explanation="The &rsquo; character entity is used to display the right single quote symbol in HTML",
        learn_more_url="https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the HTML character entity for the left double quote symbol?",
        true="&ldquo;",
        false=["&leftdouble;", "&ldquotes;", "&ldoublequo;"],
        explanation="The &ldquo; character entity is used to display the left double quote symbol in HTML",
        learn_more_url="https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the HTML character entity for the right double quote symbol?",
        true="&rdquo;",
        false=["&rdquotes;", "&rightdquo;", "&rdoublequo;"],
        explanation="The &rdquo; character entity is used to display the right double quote symbol in HTML",
        learn_more_url="https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the HTML character entity for the trademark symbol?",
        true="&trade;",
        false=["&trademark;", "&tmark;", "&trademk;"],
        explanation="The &trade; character entity is used to display the trademark symbol in HTML",
        learn_more_url="https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the HTML character entity for the copyright symbol?",
        true="&copy;",
        false=["&copyright;", "&cright;", "&copyr;"],
        explanation="The &copy; character entity is used to display the copyright symbol in HTML",
        learn_more_url="https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the HTML character entity for the degree symbol?",
        true="&deg;",
        false=["&degree;", "&d;", "&dg;"],
        explanation="The &deg; character entity is used to display the degree symbol in HTML",
        learn_more_url="https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the address tag in HTML?",
        true="a section to place address information",
        false=["a place for links", "a place for images", "a place for table data"],
        explanation="The address tag is used as a section to place address information",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html5-elements/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the blockquote tag in HTML?",
        true="a block of text that represents a quote",
        false=["a generic block container to hold other elements", "a generic inline element", "a caption for a figure element"],
        explanation="The blockquote is a block of text that represents a quote",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html5-elements/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the figcaption tag in HTML?",
        true="a text description for the content inside the figure element",
        false=["a caption for the table element", "a caption for the form element", "a caption for the div element"],
        explanation="The figcaption is a text description for the content inside the figure element",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html5-elements/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the small tag in HTML?",
        true="a tag used to represent small text for side comments or copyright information",
        false=["small text for div elements only", "small text for img tags only", "small text for h1 tags only"],
        explanation="The small tag is used to represent small text for side comments or copyright information",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html5-elements/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the time tag in HTML?",
        true="a tag used to represent the time and/or date",
        false=["used to convert minutes to seconds", "used to convert seconds to milliseconds", "used to convert hours to minutes"],
        explanation="The time tag is used to represent the time and/or date",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html5-elements/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which HTML tag is used to create an image?",
        true="<img>",
        false=["<image>", "<i>", "<hr>"],
        explanation="The <img> tag is used to add images to a website",
        learn_more_url="https://www.freecodecamp.org/news/img-html-image-tag-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these attributes does NOT work with the img tag?",
        true="capture",
        false=["src", "alt", "height"],
        explanation="The img tag can use a variety of attributes including src, alt, width, and height",
        learn_more_url="https://www.freecodecamp.org/news/img-html-image-tag-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the src attribute do in the img tag?",
        true="represents the source for the image",
        false=["provides descriptive text for the image", "provides the height of the image", "provides the width of the image"],
        explanation="The src attribute represents  the source for the image so the browser knows where to locate it",
        learn_more_url="https://www.freecodecamp.org/news/img-html-image-tag-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the alt attribute do in the img tag?",
        true="it provides a description of the image",
        false=["it provides the time when the image was taken", "it provides the source for the image", "it provides the dimensions for an image"],
        explanation="The alt attribute provides a description of the image",
        learn_more_url="https://www.freecodecamp.org/news/img-html-image-tag-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the title attribute do in the img tag?",
        true="it provides additional information about the image",
        false=["it creates a title above the img tag", "it creates a title below the img tag", "it creates a title to the left of the img tag"],
        explanation="The title attribute can be used to provide additional information about the image",
        learn_more_url="https://www.freecodecamp.org/news/img-html-image-tag-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT a supported format for the img tag?",
        true="txt",
        false=["png", "WebP", "jpeg"],
        explanation="The img tag can support many formats including WebP, JPEG and PNG",
        learn_more_url="https://www.freecodecamp.org/news/img-html-image-tag-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the pre tag in HTML?",
        true="a tag used for preformatted sections of text",
        false=["small text for h1 tags only", "a generic block container to hold other elements", "a caption for the form element"],
        explanation="The pre tag is used to display preformatted sections of text",
        learn_more_url="https://www.freecodecamp.org/news/pre-tag-in-html-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which HTML tag supports mailto links?",
        true="anchor tag",
        false=["paragraph tag", "script tag", "img tag"],
        explanation="You can create a mailto link in the href value for an anchor tag",
        learn_more_url="https://www.freecodecamp.org/news/mailto-link-how-to-make-an-html-email-link-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What property should you add to <input> to create a checkbox?",
        true="type=\"checkbox\"",
        false=["type=\"radio\"", "type=\"check\"", "type=\"button\""],
        explanation="To create a checkbox, you must add type=\"checkbox\" to the <input> tag.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox",
        difficulty=1
        ),
        QuizQuestion(
        question="What tag would you use to create a level 1 section heading? ",
        true="<h1>",
        false=["<t1>", "<1h>", "<1H>"],
        explanation="You can use the <h1> tag to create a level 1 section heading in HTML.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements",
        difficulty=1
        ),
        QuizQuestion(
        question="What property should you add to <input> to create a radio button?",
        true="type=\"radio\"",
        false=["type=\"checkbox\"", "type=\"check\"", "type=\"button\""],
        explanation="To create a radio button, you must add type=\"radio\" to the <input> tag.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the main purpose of HTML in a website?",
        true="Structure",
        false=["Style", "Functionality", "Sound"],
        explanation="HTML defines the structure of the website. ",
        learn_more_url="https://www.freecodecamp.org/news/html-crash-course/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML is used to represent the dominant content of a website?",
        true="<main>",
        false=["<dom>", "<content>", "<con>"],
        explanation="The <main> tag is used in HTML to represent the dominant content of a website.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to create an ordered list?",
        true="<ol>",
        false=["<ul>", "<img>", "<dl>"],
        explanation="The <ol> tag is used to create an ordered list in HTML.",
        learn_more_url="https://www.freecodecamp.org/news/html-list-how-to-use-bullet-points-ordered-and-unordered-lists/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to create a description list?",
        true="<dl>",
        false=["<del>", "<des>", "<d>"],
        explanation="The <dl> tag is used to create a description list in HTML.",
        learn_more_url="https://www.freecodecamp.org/news/html-list-how-to-use-bullet-points-ordered-and-unordered-lists/",
        difficulty=1
        ),
        QuizQuestion(
        question="It is recommended to write HTML tags in...",
        true="Lowercase",
        false=["Uppercase", "camelCase", "snake_case"],
        explanation="It is recommended to write HTML tags in lowercase.",
        learn_more_url="https://www.freecodecamp.org/news/the-html-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to represent a set of navigation links?",
        true="<nav>",
        false=["<navigation>", "<link>", "<navig>"],
        explanation="The <nav> tag is used to represent the main navigation functionality of a webpage.",
        learn_more_url="https://www.freecodecamp.org/news/how-to-build-a-navigation-bar/",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML tag represents a line break element?",
        true="<br>",
        false=["<hr>", "<break>", "<line>"],
        explanation="The <br> tag is used to represent a line break element.",
        learn_more_url="https://www.freecodecamp.org/news/html-line-break-how-to-break-a-line-with-the-html-br-tag/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag represents a thematic break (horizontal line) element?",
        true="<hr>",
        false=["<br>", "<line>", "<hor>"],
        explanation="The <hr> tag is used to represent a thematic break (horizontal rule) element.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to make text bold and mark it as important text?",
        true="<strong>",
        false=["<b>", "<em>", "<bold>"],
        explanation="The <strong> tag is used to make text bold and to indicate that the text is important.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to make text italic without emphasis on its content?",
        true="<i>",
        false=["<em>", "<b>", "<italic>"],
        explanation="The <i> tag is used to make text italic without adding extra emphasis. It is commonly used for text that is set off from normal prose, like foreign words or thoughts. ",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em#i_vs._em",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to make text italic with emphasis on its content?",
        true="<em>",
        false=["<i>", "<b>", "<italic>"],
        explanation="The <em> tag is used to make text italic with extra emphasis on its content.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to make inline text be displayed as superscript?",
        true="<sup>",
        false=["<super>", "<sub>", "<s>"],
        explanation="The <sup> tag displays inline text as superscript.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML tag is used to make inline text be displayed as subscript?",
        true="<sub>",
        false=["<subs>", "<s>", "<sup>"],
        explanation="The <sub> tag displays inline text as subscript.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML tag is used to represent an abbreviation or acronym?",
        true="<abbr>",
        false=["<abr>", "<abbreviation>", "<acr>"],
        explanation="The <abbr> tag is used to represent abbreviations or acronyms in HTML.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML tag is used to create a table?",
        true="<table>",
        false=["<t>", "<tbl>", "<ta>"],
        explanation="The <table> tag is used to create a table in HTML.",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to create a row in a table?",
        true="<tr>",
        false=["<trow>", "<th>", "<td>"],
        explanation="The <tr> tag is used to create a row in a table.",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to create a column (cell) in a table?",
        true="<td>",
        false=["<table>", "<tcol>", "<col>"],
        explanation="The <td> tag is used to create a column (cell) in a table.",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to create a header in a table?",
        true="<th>",
        false=["<header>", "<theader>", "<td>"],
        explanation="The <th> tag is used to create a header in a table.",
        learn_more_url="https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does DOM stand for?",
        true="Document Object Model",
        false=["Direct Object Model", "Document Objective Model", "Documentary Object Mobile"],
        explanation="DOM stands for Document Object Model.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/#:~:text=DOM%20stands%20for%20Document%20Object,remove%20elements%20from%20the%20document.",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML tag is used to taget specific inline content such as text?",
        true="<span>",
        false=["<div>", "<s>", "<i>"],
        explanation="The <span> tag is used to target specific inline content such as text. This is helpful when you want to style only certains parts of the text.",
        learn_more_url="https://www.freecodecamp.org/news/span-html-how-to-use-the-span-tag-with-css/",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML tag is used to embed video?",
        true="<video>",
        false=["<vid>", "<v>", "<player>"],
        explanation="The <video> tag is used to embed video in an HTML document.",
        learn_more_url="https://www.freecodecamp.org/news/html5-video/",
        difficulty=2
        ),
        QuizQuestion(
        question="What attribute can you add to a <video> tag to add the browser's default video controls to the embedded video?",
        true="controls",
        false=["control", "c", "basiccontrols"],
        explanation="The controls attribute adds the browser's basic video controls to the embedded video.",
        learn_more_url="https://www.freecodecamp.org/news/html5-video/",
        difficulty=2
        ),
        QuizQuestion(
        question="What is metadata in an HTML file?",
        true="Information about the webpage that is not directly displayed.",
        false=["Information about the users of the website", "Information about the server that hosts the webpage.", "Information about the version of CSS being used."],
        explanation="Metadata is information about the webpage that is not directly displayed. This includes information about its title, scripts, stylesheets, and author information.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML tag is used to create a form?",
        true="<form>",
        false=["<f>", "<th>", "<table>"],
        explanation="The <form> tag is used to create a form. ",
        learn_more_url="https://www.freecodecamp.org/news/html-form-input-type-and-submit-button-example/",
        difficulty=1
        ),
        QuizQuestion(
        question="What attribute can you add to <input> to create an input field for a password?",
        true="type=\"password\"",
        false=["type=\"pass\"", "type=\"secret\"", "type=\"hide\""],
        explanation="The type=\"password\" attribute is used to create an input field for a password (the characters will be hidden).",
        learn_more_url="https://www.freecodecamp.org/news/html-form-input-type-and-submit-button-example/",
        difficulty=1
        ),
        QuizQuestion(
        question="What attribute can you add to <input> to define a range of valid values for the user input?",
        true="type=\"range\"",
        false=["type=\"r\"", "type=\"maxmin\"", "type=\"number\""],
        explanation="The type=\"range\" attribute is used to create an input field that takes a numerical value within a certain range.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range",
        difficulty=1
        ),
        QuizQuestion(
        question="What attribute can you add to <input> to create a checkbox?",
        true="type=\"checkbox\"",
        false=["type=\"c\"", "type=\"box\"", "type=\"form\""],
        explanation="The type=\"checkbox\" attribute is used to create a checkbox in HTML.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox",
        difficulty=1
        ),
        QuizQuestion(
        question="What attribute can you add to <input> to create a submit button?",
        true="type=\"submit\"",
        false=["type=\"send\"", "type=\"end\"", "type=\"receive\""],
        explanation="The type=\"submit\" attribute is used to create a submit button in HTML.",
        learn_more_url="https://www.freecodecamp.org/news/html-form-input-type-and-submit-button-example/",
        difficulty=1
        ),
        QuizQuestion(
        question="What HTML attribute can you add to <input> to match a pattern with a regular expression?",
        true="pattern",
        false=["regex", "match", "find"],
        explanation="The pattern attribute is used to check for a pattern in a text field. You can assign a regular expression to this attribute to define the pattern.",
        learn_more_url="https://www.freecodecamp.org/news/form-validation-with-html5-and-javascript/",
        difficulty=3
        ),
        QuizQuestion(
        question="What HTML attribute should you add to set a maximum value for a numerical <input> field?",
        true="max",
        false=["maximum", "min", "top"],
        explanation="The max attribute is used to set a maximum value allowed for user input in a numerical input field.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#attributes",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML attribute should you add to set a minimum value for a numerical <input> field?",
        true="min",
        false=["minimum", "max", "bottom"],
        explanation="The min attribute is used to set a minimum value allowed for user input in a numerical input field.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#attributes",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML attribute is used to make an <input> field required?",
        true="required",
        false=["mandatory", "must", "fixed"],
        explanation="The required attribute is used to make an <input> field required to submit a form.",
        learn_more_url="https://www.freecodecamp.org/news/form-validation-with-html5-and-javascript/",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML tag is used to embed audio into a document?",
        true="<audio>",
        false=["<video>", "<sound>", "<mp3>"],
        explanation="The <audio> tag is used to embed audio into a document. ",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML tag is used to represent a section quotes from another source?",
        true="<blockquote>",
        false=["<quote>", "<q>", "<section>"],
        explanation="The <blockquote> tag is used to represent a section quotes from another source.",
        learn_more_url="https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/",
        difficulty=2
        ),
        QuizQuestion(
        question="What HTML element is a generic container for other HTML elements?",
        true="<div>",
        false=["<p>", "<a>", "<img>"],
        explanation="A div is the HTML element that serves as a generic container for other HTML elements.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div",
        difficulty=2
        )
    ]

    it_questions = [

        QuizQuestion(
        question="What does DNS do?",
        true="Maps domain names to IP addresses",
        false=["Is responsible for encrypting HTTP connections", "Provides the web client with web files during client-server communication", "Breaks down web information into smaller chunks, or packets"],
        explanation="The Domain Name System (DNS) maps human-readable domain names to IP addresses(unique identifiers). For example, DNS translates and maps the domain freecodecamp.org to the IP address 104.26.2.33.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-dns/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which port is used for HTTP?",
        true="80",
        false=["443", "40", "60"],
        explanation="By default HTTP Port-80 is used for HTTP(which stands for HyperText Transfer Protocol)",
        learn_more_url="https://www.freecodecamp.org/news/what-is-https-http-vs-https-meaning-and-how-it-works/",
        difficulty=2
        ),
        QuizQuestion(
        question="What does DNS stand for?",
        true="Domain Name system",
        false=["Dynamic Name System", "Domain Naming System", "Domain Network System"],
        explanation="DNS is an abbreviation for Domain Name System",
        learn_more_url="https://www.freecodecamp.org/news/what-is-dns/",
        difficulty=2
        ),
        QuizQuestion(
        question="How many versions of the Internet Protocol are there?",
        true="1",
        false=["4", "6", "2"],
        explanation="IPv4 is the first, and most widely used, version of the Internet Protocol. IPv6 is the latest version of the Internet Protocol. It's the successor of IPv4 and there will be a slow shift towards it in the future.",
        learn_more_url="https://www.freecodecamp.org/news/ipv4-vs-ipv6-what-is-the-difference-between-ip-addressing-schemes/",
        difficulty=2
        ),
        QuizQuestion(
        question="How many bits are there in an IPv6 address?",
        true="128",
        false=["32", "126", "64"],
        explanation="IPv6 is a 128-bit address, meaning that there are 2^128 addresses available.",
        learn_more_url="https://www.freecodecamp.org/news/ipv4-vs-ipv6-what-is-the-difference-between-ip-addressing-schemes/",
        difficulty=2
        ),
        QuizQuestion(
        question="How many bits are there in an IPv4 address?",
        true="32",
        false=["64", "16", "8"],
        explanation="IPv4 is a 32-bit address and it's made up of 4 blocks – with each block being separated by a dot, and looks something like this: XXX.XXX.XXX.XXX",
        learn_more_url="https://www.freecodecamp.org/news/ipv4-vs-ipv6-what-is-the-difference-between-ip-addressing-schemes/",
        difficulty=2
        ),
        QuizQuestion(
        question="What does HTTPS stand for?",
        true="HyperText Transfer Protocol Secure",
        false=["HyperText Transfer Protocol Standard", "HyperTransfer Text Protocol Secure", "HyperText Transfer Protocol Set"],
        explanation="HTTPS is a secure way of transferring data between a web server and a web browser",
        learn_more_url="https://www.freecodecamp.org/news/what-is-https-http-vs-https-meaning-and-how-it-works/",
        difficulty=2
        ),
        QuizQuestion(
        question="What's the difference between HTTP and HTTPS?",
        true="HTTPS is the secure version of HTTP. It's HTTP with encryption",
        false=["HTTP sends HyperText data between a web server and a web browser and HTTPS doesn't", "There is no difference", "SSL certificates are required for HTTP, but not for HTTPS"],
        explanation="HTTPS is the secure version of HTTP, the basic network protocol for sending hypertext over the web. In HTTPS there are additional steps for security, such as TSL/SSL certificates and the TSL/SSL handshake.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-https-http-vs-https-meaning-and-how-it-works/",
        difficulty=2
        ),
        QuizQuestion(
        question="What is the Internet?",
        true="Loads of wires and undersea cables connected and buried deep in the ground and oceans, all around the world.",
        false=["A cloud", "Another term for the World Wide Web", "An executable program file"],
        explanation="The Internet is actually a wire. Well, many wires that connect computers all around the world. The Internet is also infrastructure. It's a global network of interconnected computers that communicate through a standardised way with set protocols.",
        learn_more_url="https://www.freecodecamp.org/news/brief-history-of-the-internet/",
        difficulty=2
        ),
        QuizQuestion(
        question="What does CPU stand for?",
        true="Central Processing Unit",
        false=["Central Protocol Unit", "Central Programming Unit", "Control Processing Unit"],
        explanation="HTTPS is the secure version of HTTP, the basic network protocol for sending hypertext over the web. In HTTPS there are additional steps for security, such as TLS/SSL certificates and the TLS/SSL handshake.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-cpu-meaning-definition-and-what-cpu-stands-for/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which part of the CPU is responsible for carrying out mathematical operations?",
        true="The Arithmetic Logic Unit",
        false=["The Control Unit", " Registers", "Cache Memory"],
        explanation="The ALU(short for Control Unit) is a digital circuit that performs arithmetic operations such as addition, subtraction, multiplication, and division",
        learn_more_url="https://www.freecodecamp.org/news/what-is-cpu-meaning-definition-and-what-cpu-stands-for/",
        difficulty=2
        ),
        QuizQuestion(
        question="What CPU component is responsible for comparing data?",
        true="The Arithmetic Logic Unit",
        false=["The Control Unit", "Registers", "RAM"],
        explanation="The ALU (short for Arithmetic Logic Unit), is the part where all mathematical calculations take place, such as addition, subtraction, multiplication, and division, as well as all the logical operations for decision making, such as comparing data.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-cpu-meaning-definition-and-what-cpu-stands-for/",
        difficulty=2
        ),
        QuizQuestion(
        question="What are registers inside a CPU responsible for?",
        true="They temporarily hold data the CPU needs fast access to",
        false=["They help improve the speed of your computer", "They check and confirm every process that is happening on your computer", "They are responsible for carrying out all mathematical and logical operations"],
        explanation="Registers are an extremely fast memory location. The data and instructions that are being processed during the fetch-execute cycle  a CPU performs are stored there, for quick access by the processor.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-cpu-meaning-definition-and-what-cpu-stands-for/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which of the following is NOT considered a piece of computer hardware?",
        true="The Operating System  ",
        false=["The CPU(Central Processing Unit)", "The keyboard", "The mouse"],
        explanation="Hardware are the physical components you can touch, and they are located on both the outside and the inside of a computer.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-pc-computer-definition-and-computer-basics-for-beginners/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which of the following is considered an example of an input device?",
        true="A computer mouse",
        false=["Speakers", "Monitor", "Projector"],
        explanation="Examples of Input devices are a keyboard(used for typing text and characters – essentially for entering any written information), a mouse f(or clicking, pointing, and selecting appropriate data) and a microphone.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-pc-computer-definition-and-computer-basics-for-beginners/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which hardware component has all of its data wiped when the power turns off? ",
        true="RAM(Random Access Memory)",
        false=["HDD(Hard Disk Drive)", "SSD(Solid State Drive)", "CPU (Central Processing Unit)"],
        explanation="RAM ( short for Random Access Memory), or the main memory, is a volatile, short-term type of memory that only stores information temporarily while a computer is powered by electricity. It is used when you open and are using an application or file. When the power turns off, any files you created or updates you made and didn't save, will be lost and will be hard to retrieve.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-pc-computer-definition-and-computer-basics-for-beginners/",
        difficulty=2
        ),
        QuizQuestion(
        question="Where is the CPU located on a computer?",
        true="The motherboard",
        false=["Graphics Processing Unit", "Random Access Memory", "Solid State Drive"],
        explanation="The CPU is located on the motherboard of a computer.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-cpu-meaning-definition-and-what-cpu-stands-for/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does a CPU do?",
        true="A CPU executes commands from a computer program",
        false=["Writes code for developers", "Displays images and text on screen", "A device that points to objects on the screen"],
        explanation="The CPU is the brains of a computer that processes operations and executes instructions for computer programs. ",
        learn_more_url="https://www.freecodecamp.org/news/what-is-cpu-meaning-definition-and-what-cpu-stands-for/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT a main component of a CPU?",
        true="AXLE",
        false=["Control Unit", "Arithmetic Logic Unit", "Registers"],
        explanation="The Control Unit, Arithmetic Logic Unit, and Registers are important parts of the CPU. ",
        learn_more_url="https://www.freecodecamp.org/news/what-is-cpu-meaning-definition-and-what-cpu-stands-for/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT an internal piece of hardware in a computer?",
        true="GAMMA",
        false=["motherboard", "Central Processing Unit", "Graphics Processing Unit"],
        explanation="Some important pieces of a computer's internal hardware include a motherboard, CPU, GPU, RAM and HDD.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-pc-computer-definition-and-computer-basics-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What do HDD and SSD stand for in computer hardware?",
        true="Hard Disk Drive & Solid State Drive",
        false=["Harvest Disk Drive & Solid State Drive", "Hard Disk Drive & Segment State Drive", "Hard Disk Drive & Scratch State Drive"],
        explanation="HDD stands for Hard Disk Drive while SSD stands for Solid State Drive.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-pc-computer-definition-and-computer-basics-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT a popular operating system for computers?",
        true="PASSIM",
        false=["Microsoft Windows", "Apple OS", "Linux"],
        explanation="Linux, Microsoft Windows and Apple are three types of popular operating systems used by developers",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-pc-computer-definition-and-computer-basics-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is an operating system?",
        true="Manages the hardware and software components of a computer",
        false=["A program that translates code from one languages to another", "A system that converts data into machine code", "A base 2 numerical system made up of 0's and 1's"],
        explanation="An operating system manages the hardware and software components of a computer.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-pc-computer-definition-and-computer-basics-for-beginners/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a Solid State Drive?",
        true="A type of storage device that uses flash memory to store and access data",
        false=["A device to record text to a disk", "A device to translate code from one language to another ", "A screen editor used for Unix"],
        explanation="A type of storage device that uses flash memory to store and access data",
        learn_more_url="https://www.freecodecamp.org/news/ssd-solid-state-drive-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a Hard Disk Drive? ",
        true="A type of storage device that holds data including the operating system, applications, and files",
        false=["A device to record sound to a disk", "A device for the computer's short term memory", "A port used to connect to a computer to other devices"],
        explanation="A type of storage device that holds data including the operating system, applications, and files",
        learn_more_url="https://www.freecodecamp.org/news/hdd-hard-disk-drive-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is RAM?",
        true="A type of short term memory that stores data that computer processors need access to",
        false=["A type of memory that computers use to call servers", "A type of memory that computers use to delete data", "A type of memory that computers use to connect with other devices"],
        explanation="Random Access Memory is a type of short term memory that stores data that computer processors can access frequently",
        learn_more_url="https://www.freecodecamp.org/news/ram-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is PRAM?",
        true="A battery powered RAM for older Mac computers that holds important information for your system",
        false=["A newer type of RAM for Mac computers", "A newer type of RAM for Windows Computers", "A battery powered RAM for older PC computers that holds important information for your system"],
        explanation="Parameter Random Access Memory is a battery powered RAM for older Mac computers that holds important information for your system",
        learn_more_url="https://www.freecodecamp.org/news/pram-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a Subnet Mask?",
        true="Creates a range for IP addresses used in a subnet",
        false=["A type of software life cycle described by W. W. Royce", "A devices that performs restricted operations on time-sharing systems", "A device that reboots the system"],
        explanation="A Subnet Mask is used to creates a range for IP addresses used in a subnet. ",
        learn_more_url="https://www.freecodecamp.org/news/subnet-mask-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a Subnet?",
        true="A smaller network that is nested inside a large network.",
        false=["A protocol that sends and receives data from a remote device", "A protocol that assures accurate time by referring to clocks on the internet", "A feature that allows users to access remote services"],
        explanation="A Subnet is a smaller network that is nested inside a large network.",
        learn_more_url="https://www.freecodecamp.org/news/subnet-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a Ping?",
        true="The process of sending signals to other devices and waiting for a response",
        false=["A protocol that allows users to send files from one computer to another", "A way to share a single processor for multiple independent jobs", "A portion of memory used to store messages"],
        explanation="A ping is the process of sending signals to other devices and waiting for a response",
        learn_more_url="https://www.freecodecamp.org/news/ping-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does URL stand for?",
        true="Universal Resource Locator",
        false=["Unified Resource Locator", "Universal Redirect Locator", "Universal Resource Label"],
        explanation="URL stands for Universal Resource Locator and it serves as the location of an online resource",
        learn_more_url="https://www.freecodecamp.org/news/url-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many bytes make up a Yottabyte?",
        true="1 septillion bytes",
        false=["1 thousand bytes", "1 million bytes", "1 billion bytes"],
        explanation="A Yottabyte is made up of 1 septillion bytes",
        learn_more_url="https://www.freecodecamp.org/news/yottabyte-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many bytes make up a Zettabyte?",
        true="1 sextillion bytes",
        false=["1 Hundred bytes", "1 Thousand bytes", "1 million bytes"],
        explanation="A Zettabyte is composed of 1 sextillion bytes",
        learn_more_url="https://www.freecodecamp.org/news/zettabyte-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many bytes make up a Exabyte?",
        true="1 quintillion bytes",
        false=["1 Billion bytes", "1 Trillion bytes", "1 Thousand bytes"],
        explanation="A Exabyte is composed of 1 quintillion bytes",
        learn_more_url="https://www.freecodecamp.org/news/exabyte-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many bytes make up a Petabyte?",
        true="1 quadrillion bytes",
        false=["1 quintillion bytes", "1 Hundred bytes", "1 million bytes"],
        explanation="A Petabyte is composed of 1 quadrillion bytes",
        learn_more_url="https://www.freecodecamp.org/news/petabyte-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many bytes make up a Terabyte?",
        true="1 trillion bytes",
        false=["1 Billion bytes", "1 Thousand bytes", "1 million bytes"],
        explanation="A Terabyte is composed of 1 trillion bytes",
        learn_more_url="https://www.freecodecamp.org/news/terabyte-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many bytes make up a Gigabyte?",
        true="1 billion bytes",
        false=["1 quintillion bytes", "1 Trillion bytes", "1 hundred bytes"],
        explanation="A Gigabyte is composed of 1 billion bytes",
        learn_more_url="https://www.freecodecamp.org/news/gigabyte-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many bytes make up a Megabyte?",
        true="1 million bytes",
        false=["1 thousand bytes", "1 billion bytes", "1 trillion bytes"],
        explanation="A Megabyte is composed of 1 million bytes",
        learn_more_url="https://www.freecodecamp.org/news/megabyte-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many bytes make up a Kilobyte?",
        true="1,000 bytes",
        false=["100 bytes", "10 bytes", "1 byte"],
        explanation="A Kilobyte is composed of 1,000 bytes",
        learn_more_url="https://www.freecodecamp.org/news/kilobyte-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many bits make up a byte?",
        true="8 bits",
        false=["16 bits", "32 bits", "12 bits"],
        explanation="There are 8 bits in a byte",
        learn_more_url="https://www.freecodecamp.org/news/byte-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a bit?",
        true="Smallest form of data on a computer",
        false=["Structured assembly language ", "A special type of file system", "A special type of object"],
        explanation="A binary digit or \"bit\" is the smallest form of data on a computer",
        learn_more_url="https://www.freecodecamp.org/news/bit-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a password?",
        true="A secret set of characters",
        false=["A way to request data from a server", "A special type of computer memory", "A type of array"],
        explanation="A password is a secret set of characters used to login in to applications",
        learn_more_url="https://www.freecodecamp.org/news/password-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a username?",
        true="A unique name for a user on a website",
        false=["A secret set of characters", "A data type", "A special type of object"],
        explanation="A unique name for a user on a website",
        learn_more_url="https://www.freecodecamp.org/news/username-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is P2P?",
        true="A network where two devices communicate directly",
        false=["A way to request data from a server", "A special type of file system", "A special programming library"],
        explanation="Peer to Peer or \"P2P\" is a network where two devices communicate directly",
        learn_more_url="https://www.freecodecamp.org/news/p2p-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does LCD stand for?",
        true="Liquid Crystal Display",
        false=["Label Crystal Display", "Liquid Cache Display", "Liquid Crystal Dictionary"],
        explanation="Liquid Crystal Display using Liquid Crystals to display images",
        learn_more_url="https://www.freecodecamp.org/news/lcd-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a server?",
        true="A software or hardware device that sends data over a network",
        false=["A Python library", "A type of compiler", "An IDE"],
        explanation="A server is a software or hardware device that sends data over a network",
        learn_more_url="https://www.freecodecamp.org/news/server-definition/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does TCP stand for?",
        true="Transmission Control Protocol",
        false=["Terabyte Control Protocol", "Transmission Carrier Protocol", "Transmission Control Patch"],
        explanation="Transmission Control Protocol or \"TCP\" is a type of networking protocol online",
        learn_more_url="https://www.freecodecamp.org/news/tcp-vs-udp/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does UDP stand for?",
        true="User Datagram Protocol",
        false=["Unified Datagram Protocol", "User Database Protocol", "User Datagram Patch"],
        explanation="User Datagram Protocol of \"UDP\" is a type of connectionless protocol online",
        learn_more_url="https://www.freecodecamp.org/news/tcp-vs-udp/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which protocol secures communication between computer networks?",
        true="HTTPS ",
        false=["HTTP", "FTP", "SMTP"],
        explanation="HTTPS is a connectionless text-based protocol which offers encryption and authentication. It runs with TLS or SSL over it. TLS and SSL are practically the same thing- they both use asymmetric encryption to set up a link between the two servers using private/public keys.",
        learn_more_url="https://www.freecodecamp.org/news/wtf-is-https/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which protocol is used for transferring computer files over a network?",
        true="FTP",
        false=["SMTP", "PTP", "POP"],
        explanation="File Transfer Protocol (FTP) — is a standard protocol used for transferring files between a client and a server over a network.",
        learn_more_url="https://www.freecodecamp.org/news/http-and-everything-you-need-to-know-about-it/",
        difficulty=2
        ),
        QuizQuestion(
        question="What unit is used  for measuring the speed of the CPU?",
        true="GHz (gigahertz)",
        false=["MHz (megahertz)", "kHz (kilohertz)", "THz (terahertz)"],
        explanation="The speed of a computer is determined by its clock cycle. The clock speed measures the number of cycles the CPU executes per second. Hertz is a unit of frequency.  The CPU clock cycle is measured  in GHz(gigahertz). 1GHz is equal to 10 ⁹ Hz(hertz).So 1gigahertz means 10 ⁹ cycles per second.",
        learn_more_url="https://www.freecodecamp.org/news/how-does-a-cpu-work/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which of the following is an example of volatile memory?",
        true="RAM(Random Access Memory)",
        false=["SSD(Solid State Drive)", "MRAM ", "ROM"],
        explanation="While RAM is very fast, it is a type of volatile memory. This means that it only stores information while the computer is on. Unlike an HDD or SSD, once you shut down your computer, everything stored in RAM is lost.",
        learn_more_url="https://www.freecodecamp.org/news/ram-definition/",
        difficulty=2
        ),
        QuizQuestion(
        question="What is another term used when referring to the CPU?",
        true="Processor",
        false=["Operating System", "System Unit", " Computer Software"],
        explanation="CPU is short for Central Processing Unit. It is also known as a processor or microporcessor.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-cpu-meaning-definition-and-what-cpu-stands-for/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which is layer 1 in the OSI model?",
        true="The physical layer",
        false=["The network layer", "The transport Layer", "The application layer"],
        explanation="Layer 1 is the physical layer.There’s a lot of technology in Layer 1 - everything from physical network devices, cabling, to how the cables hook up to the devices.",
        learn_more_url="https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/",
        difficulty=3
        ),
        QuizQuestion(
        question="Which OSI layer is responsible for error detection?",
        true="The data link layer",
        false=["The transport layer", "The network layer", "The physical layer"],
        explanation="The the data link layer is layer 2 in the OSI model. Layer 2 defines how data is formatted for transmission, how much data can flow between nodes, for how long, and what to do when errors are detected in this flow.",
        learn_more_url="https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/",
        difficulty=3
        ),
        QuizQuestion(
        question="Which OSI layer is responsible for logical addressing and routing?",
        true="The network layer",
        false=["The presentation layer", "The session layer", "The transport layer"],
        explanation="The network layer is layer 3 of the OSI model. This is where we send information between and across networks through the use of routers. ",
        learn_more_url="https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/",
        difficulty=3
        ),
        QuizQuestion(
        question="Which OSI layer is responsible for providing reliable end to end communication?",
        true="The transport layer",
        false=["The physical layer", "The data link layer", "The session layer"],
        explanation="The Transport Layer is layer 4 of the OSI model and provides end-to-end transmission of a message by segmenting a message into multiple data packets; the layer supports connection-oriented and connectionless communication.",
        learn_more_url="https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/",
        difficulty=3
        ),
        QuizQuestion(
        question="Which OSI layer is responsible for establishing,maintaining and terminating  a communication session?",
        true="Layer 5",
        false=["Layer 1", "Layer 4", "Layer 3"],
        explanation="Layer 5 is the session layer. This layer establishes, maintains, and terminates sessions.",
        learn_more_url="https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/",
        difficulty=3
        ),
        QuizQuestion(
        question="Which OSI layer is responsible for data compression and encryption?",
        true="The presentation layer",
        false=["The application layer", "layer 1", "layer 5"],
        explanation="The presentation layer is layer 6 in the OSI model. This layer is responsible for data formatting, such as character encoding and conversions, and data encryption.",
        learn_more_url="https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/",
        difficulty=3
        ),
        QuizQuestion(
        question="which OSI layer is responsible for email and file transfers?",
        true="The application layer",
        false=["The network layer", "The session layer ", "The presentation layer"],
        explanation="Layer 7 is the application layer. Electronic mail programs, for example, are specifically created to run over a network and utilize networking functionality, such as email protocols, which fall under Layer 7. ",
        learn_more_url="https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/",
        difficulty=3
        ),
        QuizQuestion(
        question="What does IP stand for?",
        true="Internet Protocol",
        false=["Interconnection Protocol", "International Passenger", "Internal Product"],
        explanation="The IP address is a special number that makes sure that the information sent through the internet reaches the right destination. ",
        learn_more_url="https://www.freecodecamp.org/news/what-is-my-ip-address-for-my-router-how-to-find-your-wifi-address/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does HTTP stand for?",
        true="HyperText Transfer Protocol",
        false=["HyperText Transmission Protocol", "HyperTest Transfer Product", "HyperText Transfer Password"],
        explanation="HTTP stands for HyperText Transfer Protocol.",
        learn_more_url="https://www.freecodecamp.org/news/http-and-everything-you-need-to-know-about-it/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does WWW stand for?",
        true="World Wide Web",
        false=["World Web Wide", "Wide World Web", "World World Web"],
        explanation="WWW stands for World Wide Web.",
        learn_more_url="https://www.britannica.com/topic/World-Wide-Web",
        difficulty=1
        ),
        QuizQuestion(
        question="Who invented the World Wide Web?",
        true="Tim Berners-Lee",
        false=["Ada Lovelace", "Alan Turing", ""],
        explanation="Tim Berners-Lee invented the World Wide Web in 1989.",
        learn_more_url="https://en.wikipedia.org/wiki/Tim_Berners-Lee",
        difficulty=1
        ),
        QuizQuestion(
        question="When was the World Wide Web invented?",
        true="1989",
        false=["1990", "1995", "2005"],
        explanation="Tim Berners-Lee invented the World Wide Web in 1989.",
        learn_more_url="https://en.wikipedia.org/wiki/World_Wide_Web",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a virtual machine?",
        true="A computer inside another computer",
        false=["an Operating system", "a Linux distribution", "another name for a compiler"],
        explanation="A virtual machine is a program you run on a computer that acts like it is a separate computer. It is basically a way to create a computer within a computer.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-virtual-machine-and-how-to-setup-a-vm-on-windows-linux-and-mac/",
        difficulty=2
        ),
        QuizQuestion(
        question="What does GIF stand for?",
        true="Graphics Interchange Format",
        false=["Graphical International Format", "Graphical Interconnected Functions", "General Interchange Format"],
        explanation="GIF stands for Graphics Interchange Format.",
        learn_more_url="https://www.freecodecamp.org/news/how-to-make-a-gif-create-animated-gifs-without-downloading-software/#:~:text=A%20GIF%20(Graphics%20Interchange%20Format,with%20your%20friends%20and%20family.",
        difficulty=1
        ),
        QuizQuestion(
        question="What does JPEG stand for?",
        true="Join Photographic Experts Group",
        false=["Join Photogenic Experimental Group", "Join Photographic External Graphics", "Join Photos Enchanted Graphics"],
        explanation="JPEG stands for Join photographic Experts Group.",
        learn_more_url="https://en.wikipedia.org/wiki/JPEG",
        difficulty=1
        ),
        QuizQuestion(
        question="What does PNG stand for?",
        true="Portable Network Graphics",
        false=["Portable New Graphics", "Premium Network Graphics", "Portable Network Green"],
        explanation="PNG stands for Portable Network Graphics.",
        learn_more_url="https://en.wikipedia.org/wiki/Portable_Network_Graphics",
        difficulty=1
        ),
        QuizQuestion(
        question="What does SVG stand for?",
        true="Scalable Vector Graphics",
        false=["Stretchable Vector Graphics", "Scalable Vectorial Graphics", "Screen Vector Graphics"],
        explanation="SVG stands for Scalable Vector Graphics.",
        learn_more_url="https://www.freecodecamp.org/news/use-svg-images-in-css-html/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does API stand for?",
        true="Application Programming Interface",
        false=["Apple Pie Inside", "Application Program Interface", "Another Program Interface"],
        explanation="API stands for Application Programming Interface.",
        learn_more_url="https://www.freecodecamp.org/news/what-does-api-stand-for-a-definition-of-the-coding-acronym-in-plain-english/",
        difficulty=2
        ),
        QuizQuestion(
        question="An application software for accessing the World Wide Web is known as...",
        true="Browser",
        false=["IDE", "API", "Bug"],
        explanation="An application software for accessing the World Wide Web is known as browser.",
        learn_more_url="https://www.freecodecamp.org/news/web-application-security-understanding-the-browser-5305ed2f1dac/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does ISP stand for?",
        true="Internet Service Provider",
        false=["Internet System Provider", "International Service Provider", "Intermediate Systems Provider"],
        explanation="ISP stands for Internet Service Provider.",
        learn_more_url="https://www.freecodecamp.org/news/how-does-the-internet-work/",
        difficulty=1
        )
    ]

    javascript_questions = [

        QuizQuestion(
        question="What was JavaScript originally called when it was first released?",
        true="Mocha",
        false=["LiveScript", "Java", "Netscape"],
        explanation="When JavaScript first came out it was called Mocha, then later changed to LiveScript and finally settled on JavaScript.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-javascript-javascript-code-explained-in-plain-english/",
        difficulty=3
        ),
        QuizQuestion(
        question="How do you write an inline comment in JavaScript?",
        true="// Comment",
        false=["/* Comment", "# Comment", "<!-- Comment -->"],
        explanation="In JavaScript, an inline comment starts with //",
        learn_more_url="https://forum.freecodecamp.org/t/freecodecamp-challenge-guide-comment-your-javascript-code/16783",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the JavaScript keyword used to define a constant?",
        true="const",
        false=["var", "let", ""],
        explanation="The keyword const is used to define a constant in JavaScript. The value of a constant can't be changed through reassignment.",
        learn_more_url="https://www.freecodecamp.org/news/javascript-variables-beginners-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you get the length of a string in Python?",
        true=".length",
        false=["len()", "length()", ".size()"],
        explanation="Strings have a .length property that contains their length (number of characters).",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length",
        difficulty=1
        ),
        QuizQuestion(
        question="What JavaScript method adds an element to the end of an array?",
        true=".push()",
        false=[".pop()", ".shift()", ".unshift()"],
        explanation="The .push() method adds the elements passed as argument to the end of the array.",
        learn_more_url="https://www.freecodecamp.org/news/the-javascript-array-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="What JavaScript method removes the last element of an array and returns it?",
        true=".pop()",
        false=[".push()", ".shift()", ".unshift()"],
        explanation="The .pop() method removes the last element of an array and returns it.",
        learn_more_url="https://www.freecodecamp.org/news/the-javascript-array-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="What JavaScript method removes the first element of an array and returns it?",
        true=".shift()",
        false=[".push()", ".pop()", ".unshift()"],
        explanation="The .shift() removes the first element of an array and returns it. ",
        learn_more_url="https://www.freecodecamp.org/news/the-javascript-array-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="What JavaScript method adds an element to the beginning of an array?",
        true=".unshift()",
        false=[".push()", ".pop()", ".shift()"],
        explanation="The .unshift() method adds the element passed as argument to the beginning of an array.",
        learn_more_url="https://www.freecodecamp.org/news/the-javascript-array-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="What keyword is used in JavaScript to define a function?",
        true="function",
        false=["def", "func", "fct"],
        explanation="The function keyword is used to define a function in JavaScript",
        learn_more_url="https://www.freecodecamp.org/news/what-is-a-function-javascript-function-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What value is returned by default in JavaScript when a function doesn't have a return statement?",
        true="undefined",
        false=["None", "null", "0"],
        explanation="The value undefined is returned by functions that do not have a return statement.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#description",
        difficulty=1
        ),
        QuizQuestion(
        question="Select the comparison operator that you should use if you need to compare if two values are equal or not and convert them to a common type before doing the comparison.",
        true="==",
        false=["===", "!=", "!=="],
        explanation="The == operator returns true if two values are equal and false if they are not equal. It converts the values to a common type before doing the comparison.",
        learn_more_url="https://www.freecodecamp.org/news/javascript-triple-equals-sign-vs-double-equals-sign-comparison-operators-explained-with-examples/",
        difficulty=2
        ),
        QuizQuestion(
        question="How can you convert a string to an integer in JavaScript?",
        true="parseInt()",
        false=["parseString()", "parseInteger()", "parseSrt()"],
        explanation="The parseInt() function converts the value passed as argument to an integer.",
        learn_more_url="https://www.freecodecamp.org/news/convert-string-to-number-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What JavaScript operator takes an array and spreads it into its individual elements?",
        true="Spread operator",
        false=["Rest operator", "Division Operator", "Multiplication Operator"],
        explanation="The spread operator takes an array and spreads it into its individual elements. With this operator, we can pass the elements of an array as individual arguments to a function call.",
        learn_more_url="https://www.freecodecamp.org/news/javascript-rest-vs-spread-operators/",
        difficulty=2
        ),
        QuizQuestion(
        question="What JavaScript operator allows you to create a function that takes a variable number of arguments?",
        true="Rest operator",
        false=["Spread operator", "Division Operator", "Multiplication Operator"],
        explanation="The rest operator takes the individual arguments passed to a function and converts them into an array.",
        learn_more_url="https://www.freecodecamp.org/news/javascript-rest-vs-spread-operators/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these types of loops will always run at least once in JavaScript?",
        true="Do... While Loop",
        false=["While Loop", "For Loop", ""],
        explanation="The sequence of statements in a do..while loop runs at least once because the condition is evaluated after running the statements. ",
        learn_more_url="https://www.freecodecamp.org/news/javascript-loops-explained-for-loop-for/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the main purpose of JavaScript in a website?",
        true="Functionality",
        false=["Structure", "Style", "Sound"],
        explanation="JavaScript is used to create interactive and dynamic websites.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-javascript-javascript-code-explained-in-plain-english/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the logical AND operator in JavaScript?",
        true="&&",
        false=["||", "!", "**"],
        explanation="&& is the logical AND operator in JavaScript.",
        learn_more_url="https://www.freecodecamp.org/news/javascript-logical-operators/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the logical OR operator in JavaScript?",
        true="||",
        false=["&&", "!", "**"],
        explanation="|| is the logical OR operator in JavaScript.",
        learn_more_url="https://www.freecodecamp.org/news/javascript-logical-operators/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the logical NOT operator in JavaScript?",
        true="!",
        false=["&&", "||", "%"],
        explanation="! is the logical NOT operator in JavaScript.",
        learn_more_url="https://www.freecodecamp.org/news/javascript-logical-operators/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the process that moves variables, functions and classes to the top of the scope?",
        true="hoisting",
        false=["setter", "break", "await"],
        explanation="Hoisting is the process moving variables, classes and function to the top of the scope",
        learn_more_url="https://www.freecodecamp.org/news/what-is-hoisting-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the technique used to extract array values into new variables?",
        true="array destructuring",
        false=["typeof", "async", "optional chaining"],
        explanation="Array destructuring is used  to extract array values into new variables",
        learn_more_url="https://www.freecodecamp.org/news/array-vs-object-destructuring-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the technique used to extract object values into new variables?",
        true="object destructuring",
        false=["array destructuring", "hoisting", "typeof"],
        explanation="Object destructuring is used to extract object values into new variables",
        learn_more_url="https://www.freecodecamp.org/news/array-vs-object-destructuring-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method used to see if one string is found in another?",
        true="includes",
        false=["padEnd", "slice", "trim"],
        explanation="The includes method is used to check if one string is found in another",
        learn_more_url="https://www.freecodecamp.org/news/javascript-string-contains-how-to-use-js-includes/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name for a function that is used as an argument in another function?",
        true="callback function",
        false=["arrow function", "Anonymous function", "function declaration"],
        explanation="A callback function is when a function is used as an argument in another function",
        learn_more_url="https://www.freecodecamp.org/news/javascript-callback-function-plain-english/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the DOM stand for?",
        true="Document Object Model",
        false=["Data Object Model", "Document Online Model", "Document Object Mainframe"],
        explanation="The DOM stands for Document Object Model",
        learn_more_url="https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the DOM in JavaScript?",
        true="programming interface to create, change, or remove elements from the document",
        false=["process that moves variables, functions and classes to the top of the scope", "technique used to extract array values into new variables", "a function that is used as an argument in another function"],
        explanation="The DOM is a programming interface to create, change, or remove elements from the document",
        learn_more_url="https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these methods is NOT used to select elements in the document?",
        true="typeof",
        false=["getElementById", "querySelector", "querySelectorAll"],
        explanation="There are a few methods to select elements from the document including querySelector, querySelectorAll and getElementById",
        learn_more_url="https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method used to select elements in the document by referencing the id name?",
        true="getElementById",
        false=["getElementByClass", "getId", "getElementByTagName"],
        explanation="The getElementById method is used to select elements in the document by referencing the id name",
        learn_more_url="https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to get the text content of a node?",
        true="textContent",
        false=["text-content", "content", "getContent"],
        explanation="The textContent property is used to get the text content of a node",
        learn_more_url="https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method to find elements that match one of more selectors?",
        true="querySelector",
        false=["textContent", "padEnd", "optional chaining"],
        explanation="The querySelector method is used to find elements that match one of more selectors",
        learn_more_url="https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method to find all of the elements that match the CSS selector and returns a list of all of those nodes?",
        true="querySelectorAll",
        false=["array destructuring", "includes method", "await"],
        explanation="The querySelectorAll method is used to find all of the elements that match the CSS selector and returns a list of all of those nodes",
        learn_more_url="https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method to add new elements to the DOM tree?",
        true="document.createElement()",
        false=["callback function", "querySelectorAll", "textContent"],
        explanation="The document.createElement() method is used to add new elements to the DOM tree.",
        learn_more_url="https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method to attach an event to an HTML element like a button?",
        true="addEventListener",
        false=["hoisting", "getElementById", "getElementByTagName"],
        explanation="The addEventListener method is used to attach an event to an HTML element like a button",
        learn_more_url="https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method that converts all of the letters in a string to lowercase?",
        true="toLowerCase",
        false=["toUpperCase", "toLow", "lower"],
        explanation="The toLowerCase method is used to convert all of the letters in a string to lowercase",
        learn_more_url="https://www.freecodecamp.org/news/javascript-tolowercase-how-to-convert-a-string-to-lowercase-and-uppercase-in-js/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method that converts all of the letters in a string to uppercase?",
        true="toUpperCase",
        false=["toLowerCase", "toUpper", "upper"],
        explanation="The toUpperCase method is used to convert all of the letters in a string to uppercase",
        learn_more_url="https://www.freecodecamp.org/news/javascript-tolowercase-how-to-convert-a-string-to-lowercase-and-uppercase-in-js/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method that extracts a portion of the array and returns a new array?",
        true="slice",
        false=["splice", "pop", "sort"],
        explanation="The slice method extracts a portion of the array and returns a new array",
        learn_more_url="https://www.freecodecamp.org/news/javascript-array-slice-vs-splice-whats-the-difference/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method that modifies the array in place?",
        true="splice",
        false=["slice", "push", "join"],
        explanation="The splice method modifies the array in place and can be used to remove or add elements to the array",
        learn_more_url="https://www.freecodecamp.org/news/javascript-array-slice-vs-splice-whats-the-difference/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the method that returns true if one of the elements in the callback function passes the test?",
        true="some",
        false=["findIndex", "includes", "isArray"],
        explanation="The some method returns true if one of the elements in the callback function passes the test",
        learn_more_url="https://www.freecodecamp.org/news/javascript-array-some-tutorial-how-to-iterate-through-elements-in-an-array/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT a JavaScript library?",
        true="C#",
        false=["React", "D3", "Moment"],
        explanation="There are many popular JavaScript libraries including React, D3 and Moment",
        learn_more_url="https://www.freecodecamp.org/news/10-javascript-libraries-you-should-try/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the spread operator do?",
        true="used to copy portions of an array or object into another array or object",
        false=["checks whether a certain value is present in another array", "removes the first element of the array", "returns an array of an objects keys"],
        explanation="The spread opertaor is to copy portions of an array or object into another array or object",
        learn_more_url="https://www.freecodecamp.org/news/how-to-use-es6-javascript-features-in-react/",
        difficulty=1
        ),
        QuizQuestion(
        question="What are the three ways to declare a variable in JavaScript?",
        true="var,let,const",
        false=["variable, let, const", "var, let-var, const", "var, concat, let"],
        explanation="In JavaScript, you can declare variables using var, let or const.",
        learn_more_url="https://www.freecodecamp.org/news/javascript-interview-prep-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these varaible declarations can never be re-declared within its scope?",
        true="const",
        false=["let", "var", "concat"],
        explanation="When you declare variables with const, they can never be re-declared within its scope",
        learn_more_url="https://www.freecodecamp.org/news/javascript-interview-prep-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What are the three types of scope in JavaScript?",
        true="global, function, block",
        false=["global, function,map", "reduce,function,block", "const,function,block"],
        explanation="The three types of scope in JavaScript are global, function and block",
        learn_more_url="https://www.freecodecamp.org/news/javascript-interview-prep-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What symbols are used in JavaScript to write a multiline comment?",
        true="/* */",
        false=["//", "<!-- -->", "** **"],
        explanation="In JavaScript, we use /* */ to write a multiline comment.",
        learn_more_url="https://forum.freecodecamp.org/t/freecodecamp-challenge-guide-comment-your-javascript-code/16783",
        difficulty=1
        ),
        QuizQuestion(
        question="What JavaScript keyword is used to declare a variable that can only be used in the scope of declaration?",
        true="let",
        false=["var", "const", "block"],
        explanation="In JavaScript, you can use let to declare a variable that can only be used in the scope of declaration.",
        learn_more_url="https://www.freecodecamp.org/news/javascript-variables-beginners-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="Are semicolons strictly required in JavaScript?",
        true="No",
        false=["Yes", "", ""],
        explanation="JavaScript does not require strict use of semicolons because it inserts them where they are needed through a process called Automatic Semicolon Insertion.",
        learn_more_url="https://www.freecodecamp.org/news/lets-talk-about-semicolons-in-javascript-f1fe08ab4e53/#:~:text=This%20is%20all%20possible%20because%20JavaScript%20does%20not%20strictly%20require%20semicolons.&text=It's%20important%20to%20know%20the,not%20behave%20like%20you%20expect.",
        difficulty=1
        ),
        QuizQuestion(
        question="What method joins all the elements of an array into a string in JavaScript?",
        true=".join()",
        false=[".concat()", ".fill()", ".every()"],
        explanation="The .join() method joins all the elements of an array into a string.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join",
        difficulty=1
        ),
        QuizQuestion(
        question="What string method returns the character at the specified index in JavaScript?",
        true=".charAt()",
        false=[".getChar()", ".char()", ".character()"],
        explanation="The .charAt() method returns the character at the specified index in JavaScript.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt",
        difficulty=1
        ),
        QuizQuestion(
        question="What string method combines the text of two or more strings and returns a new string?",
        true=".concat()",
        false=[".combine()", ".string()", ".join()"],
        explanation="The .concat() method combines the text of two or more strings and returns a new string.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/concat",
        difficulty=1
        )
    ]

    linux_questions = [

        QuizQuestion(
        question="Which of the following is NOT a Unix shell?",
        true="pwd",
        false=["ksh", "csh", "bash"],
        explanation="There are many different kind of shells available on Linux and macOS computers. A few of them dominate the space are bash, csh, zsh, fish and more",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#introductiontolinuxandshells",
        difficulty=1
        ),
        QuizQuestion(
        question="Which is the default shell provided with most Linux based systems?",
        true="Bourne Again SHell",
        false=["PowerSHell", "Emacs", "Fish"],
        explanation="Bash (short for Bourne Again SHell) is the most widely used shell, packaged by default for most Linux distributions",
        learn_more_url="https://www.freecodecamp.org/news/linux-command-line-bash-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command lists  the contents of a directory?",
        true="ls",
        false=["ln", "look", "less"],
        explanation="The ls command (short for list)  is used to list files or directories in Linux and other Unix-based operating systems. It  allows you to list all files or directories in the current directory",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-ls-command-how-to-list-files-in-a-directory-with-options/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the command ls -a do?",
        true="list  directories and files - including all hidden files",
        false=["list only the hidden files", "list  files and then delete them", "show deleted files"],
        explanation="The ls -a(short for all) command lists all directories(folders) and files in the current directory. This includes all hidden files. The -a flag(or option) shows hidden files. Hidden files are files that start with a dot (.)",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#introductiontolinuxandshells",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the grep command used for?",
        true="Searching through text in the given file",
        false=["Move the contents of a file to another one", "Rename the file", "Delete all text in a file"],
        explanation="grep stands for Globally Search For Regular Expression and Print out. It is a command line tool used in UNIX and Linux systems to search a specified pattern in a file or group of files.",
        learn_more_url="https://www.freecodecamp.org/news/grep-command-tutorial-how-to-search-for-a-file-in-linux-and-unix/",
        difficulty=1
        ),
        QuizQuestion(
        question="How to print all columns in a file named demo.txt using the awk command?",
        true="awk '{print $0}' demo.txt",
        false=["awk '{print $1}' demo.txt", "awk '{print $1, $2}' demo.txt", "awk '/^print/' demo.txt"],
        explanation="To print all columns and more so all the contents of a file using the awk command, the action you specify inside the curly braces is print $0.",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-awk-command-linux-and-unix-usage-syntax-examples/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which of the following is NOT a Linux distribution?",
        true="multics",
        false=["CentOS", "Debian", "RHEL"],
        explanation="There are  different versions of Linux (called distributions)  that allow the user varying degrees of personalization and control of the operating system. This means that users can choose their Linux distributions based on their wants and needs. Some popular ones are: Ubuntu, Linux Mint, CentOS, RHEL,Arch Linux",
        learn_more_url="https://www.freecodecamp.org/news/the-best-linux-tutorials/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command is used for creating files?",
        true="touch",
        false=["mv", "man", "mkdir"],
        explanation="You create an empty file using the touch command,followed by the name of the file e.g. touch demo.txt",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-touch-command",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used for creating directories(folders)?",
        true="mkdir",
        false=["mkcd", "cd", "rm"],
        explanation="You create folders using the mkdir command, followed by the name of the directory e.g. mkdir photos",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-mkdir-command",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used for creating links between files?",
        true="ln",
        false=["ls", "link", "cat"],
        explanation="The ln command is used for creating links. A link is like a pointer to another file, or a file that points to another file.",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-ln-command",
        difficulty=2
        ),
        QuizQuestion(
        question="Which flag(or option) is used with the ln command to create a soft link in Linux?",
        true="-s",
        false=["-l", "-a", "-la"],
        explanation="You create soft links using the -s option of ln. For example,ln -s <original> <link>",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-ln-command",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command deletes a directory that has NO files inside it?",
        true="rmdir",
        false=["mkdir", "rm", "touch"],
        explanation="You  delete a folder using rmdir. That folder must be empty",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-rmdir-command",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command deletes a directory with files inside it?",
        true="rm -rf",
        false=["rmdir", "rm", "ls"],
        explanation="To delete folders with files in them, you use the more generic rm command which deletes files . The -rf option is used to recursively and forcefully delete all files contained in the directory.",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-rmdir-command",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used for displaying the name of the current  user logged in the terminal?",
        true="whoami",
        false=["cat", "echo", "pwd"],
        explanation="whoami  print sthe user name currently logged in to the terminal session",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-whoami-command",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command displays information about the Operating System?",
        true="uname",
        false=["echo", "man", "find"],
        explanation="Calling uname without any options will return the Operating System codename. The m option shows the hardware name and the p option prints the processor architecture name (",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-uname-command",
        difficulty=3
        ),
        QuizQuestion(
        question="Which Linux command prints the path to the current directory you're in?",
        true="pwd",
        false=["cat", "cd", "ls"],
        explanation="pwd(short for print working directory) prints the current folder path and is helpful when you're lost in the terminal",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-pwd-command",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used for counting the total amount of lines,words and bytes in a file?",
        true="wc",
        false=["countl", "countw", "countwl"],
        explanation="The wc command gives us useful information about a file. The first column returned in the output  is the number of lines. The second is the number of words. The third is the number of bytes.",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-wc-command",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command deletes a file?",
        true="rm",
        false=["rmdir", "touch", "ls"],
        explanation="The rm (short for remove) command when used without options  delete sfiles",
        learn_more_url="https://www.freecodecamp.org/news/remove-a-directory-in-linux-how-to-delete-directories-and-contents-from-the-command-line/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Unix command opens the VIM command-line editor?",
        true="vi",
        false=["open", "open vim", "open vi"],
        explanation="You start up VIM  by running vi in the command line.",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-vim-editor-command",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Unix command is used for exiting VIM WITHOUT saving the changes you made?",
        true=":q!",
        false=[":wq", ":i", ":r"],
        explanation="If you made some changes and would rather discard them, type :q! to forcefully quit, and press Enter/return",
        learn_more_url="https://www.freecodecamp.org/news/how-to-exit-vim/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Unix command is used for exiting VIM AND saving the changes you made?",
        true=":wq",
        false=[":q!", ":h", ":j"],
        explanation="If you made some changes and would like to keep them, type :wq(short for write and quit) and press Enter/return",
        learn_more_url="https://www.freecodecamp.org/news/how-to-exit-vim/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command provides information on all other commands available?",
        true="man",
        false=["echo", "ls", "pwd"],
        explanation="The man command (short for manual),provides a manual page. The page gives you a very quick overview of a command, with some handy examples of common usage scenarios",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-man-command",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used to count JUST the lines in a file?",
        true="wc -l",
        false=["wc", "wc -w", "wc -c "],
        explanation="To count just the lines inside a file you use the wc command with the -l option",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-wc-command",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command is used to count JUST the words in a file?",
        true="wc -w",
        false=["wc -l", "wc -c", "wc   "],
        explanation="To count just the words inside a file you use the wc command with the -w option",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-wc-command",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command is used to count JUST the number of bytes in a file?",
        true="wc -c",
        false=["wc -w", "wc -l", "wc"],
        explanation="To count just the number of bytes in a file you use the wc command with the -c option",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-wc-command",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command is used to display the current running processes?",
        true="ps",
        false=["ls", "pwd", "echo"],
        explanation="You can list running processes using the ps command (ps means process status). The ps command displays your currently running processes in real-time.",
        learn_more_url="https://www.freecodecamp.org/news/linux-list-processes-how-to-check-running-processes/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Unix command is used to allow you start typing in the VIM editor?",
        true="i",
        false=["esc", ":q!", ":wq"],
        explanation="The i command( for ’insert’), immediately switches vim to insert mode. Once in insert mode, typing inserts characters just like a regular text editor",
        learn_more_url="https://www.freecodecamp.org/news/vim-editor-modes-explained/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Unix command is used to move the cursor one character to the left in the VIM editor?",
        true="h",
        false=["j", "k", "l"],
        explanation="To move the cursor one character to the left,use the h command.",
        learn_more_url="https://www.freecodecamp.org/news/vim-editor-modes-explained/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command is used to move into a directory?",
        true="cd",
        false=["mv", "pwd", "rm"],
        explanation="Once you've created a folder,you can move into it with the cd command(which stands for change directory). You invoke it specifying a folder to move into. You can specify a folder name, or an entire path.",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does .. mean in a Linux directory path?",
        true="Refers to the parent folder",
        false=["Refers to the current folder", "Refers to the home directory", "Refers to the the root of the file structure"],
        explanation="The .. is a special path  and means one level up. It refers to the the parent directory",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does . mean in a Linux directory path?",
        true="Refers to the current folder",
        false=["Refers to the parent folder", "Refers to the root of the file structure", "Refers to the home directory"],
        explanation="The . is a special path indicator. It indicates the current folder.",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which  Linux command is used to create multiple nested folders?",
        true="mkdir -p",
        false=["mkdir", "makedir", "makedir -p"],
        explanation="You create multiple nested folders by adding the -p option to the mkdir command",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used to rename files and folders?",
        true="mv",
        false=["touch", "mkdir", "rm"],
        explanation="You rename files and folders by using the mv(short for move)  command",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used to copy the contents of one file to another one?",
        true="cp",
        false=["rm ", "rmdir", "touch "],
        explanation="You copy a file using the cp command",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used to copy a whole folder and its contents?",
        true="cp -r",
        false=["cp", "mv", "mkdir"],
        explanation="To copy folders you need to add the -r option to recursively copy the whole folder contents",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which of the following Linux commands is used to showcase the contents stored in a file?",
        true="less",
        false=["open", "man", "rm"],
        explanation="The less command shows the content stored inside a file,",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used to sort  the contents of a file alphabetically and numerically?",
        true="sort",
        false=["wc", "cat", "tail"],
        explanation="The sort command helps you sort a file's contents in a particular order(either numerical or alphabetical)",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used to remove adjacent duplicate lines inside a file?",
        true="uniq",
        false=["sort", "rm", "rmdir"],
        explanation="The sort command removes duplicate lines in a file,by default",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command prints to the terminal the argument that is passed to it?",
        true="echo",
        false=["man", "print", "ls"],
        explanation="The echo command prints to the output the argument passed to it. For example, the command echo \"hello world\" will print hello world to the terminal",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command is used to change the owner of a file/directory?",
        true="chown",
        false=["uname", "whoami", "echo"],
        explanation="Every file/directory in an Operating System like Linux or macOS (and every UNIX system in general) has an owner. The owner of a file can do everything with it. It can decide the fate of that file. The owner (and the root user) can change the owner to another user, too, using the chown command:",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=3
        ),
        QuizQuestion(
        question="Which Linux command calculates the size of a directory?",
        true="du",
        false=["wc", "wc -c", "man"],
        explanation="The du command will calculate the size of a directory as a whole",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=3
        ),
        QuizQuestion(
        question="Which Linux command changes passwords for user accounts?",
        true="passwd",
        false=["chpass", "chpasswd", "cpasswd"],
        explanation="Users in Linux have a password assigned. You can change the password using the passwd command.",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=3
        ),
        QuizQuestion(
        question="Which Linux command  verifies that an IP address exists?",
        true="ping",
        false=["which", "uname", "chown"],
        explanation="The ping command pings a specific network host, on the local network or on the Internet. It verifies IP level connectivity to another computer",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=3
        ),
        QuizQuestion(
        question="Which keyboard shortcut will stop running the Linux ping command?",
        true="ctrl-C",
        false=["command-D", "ctrl-D", "exit"],
        explanation="The ping command, keeps sending multiple requests every second, by default. It will keep running until you stop it with ctrl-C",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=2
        ),
        QuizQuestion(
        question="What does GNU stand for?",
        true="GNU's not UNIX",
        false=["GeNeral Unix", "Great New Unix", "Great Needed Unix"],
        explanation="GNU is a recursive acronym for ‘GNU's not UNIX’",
        learn_more_url="https://forum.freecodecamp.org/t/the-origins-of-linux-and-the-free-software-movement-a-brief-history/19527",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command is used to remove all previous command and output from the terminal?",
        true="clear",
        false=["exit", "delete", "rm"],
        explanation="The clear  command removes all previous commands that were run in the current terminal. The screen will clear and you will just see the prompt at the top",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which Linux command shows all previous executed commands?",
        true="history",
        false=["memory", "review", "man"],
        explanation="Every time you run a command, it's memorized in the history. You can display all the history using the history command",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/",
        difficulty=1
        ),
        QuizQuestion(
        question="With which wildcard can you select ALL files in a directory?",
        true="*",
        false=["?", "[]", "!"],
        explanation="You can use the wildcard (*) to select all files in a directory. For example the ls * command would list ALL files in the current directory",
        learn_more_url="https://www.freecodecamp.org/news/grep-command-tutorial-how-to-search-for-a-file-in-linux-and-unix/",
        difficulty=2
        ),
        QuizQuestion(
        question="Which command is used to display the NAME of the operating system?",
        true="uname -s",
        false=["uname -r", "uname -k", "uname -u"],
        explanation="The s option  of the uname command prints the Operating System name",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-uname-command",
        difficulty=3
        ),
        QuizQuestion(
        question="Which command prints the Linux version?",
        true="uname -r",
        false=["uname -s", "uname -u", "uname -k"],
        explanation="The r  option of the uname command,prints the release",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-uname-command",
        difficulty=3
        ),
        QuizQuestion(
        question="Which Linux command is used to compress files?",
        true="gzip",
        false=["tar", "chown", "diff"],
        explanation="The gzip command is used to compress a file to save space",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-gzip-command",
        difficulty=2
        ),
        QuizQuestion(
        question="Which command is used to create an archive in Linux?",
        true="tar",
        false=["gzip", "gunzip", "diff"],
        explanation="The tar command is used to create an archive, grouping multiple files in a single file,without compressing them",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-tar-command",
        difficulty=2
        ),
        QuizQuestion(
        question="Which Linux command is used to send HTTP requests?",
        true="curl",
        false=["tar", "uname", "gzip"],
        explanation="Curl is a command-line tool that allows us to do HTTP requests from shell",
        learn_more_url="https://www.freecodecamp.org/news/how-to-start-using-curl-and-why-a-hands-on-introduction-ea1c913caaaa/",
        difficulty=2
        ),
        QuizQuestion(
        question="What is the main component,the \"core\", of Linux?",
        true="The kernel",
        false=["The shell", "The commands", "The terminal window"],
        explanation="The main component of linux and its core,is the kernel. It's the interface between the Operating System and all the hardware components and it manages all the processes.",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#introductiontolinuxandshells",
        difficulty=1
        ),
        QuizQuestion(
        question="Who is the creator of the Linux Operating System?",
        true="Linus Torvalds",
        false=["Bill Gates", "Mark Zuckerberg", "Sergey Brin"],
        explanation="Linus Torvalds created Linux as a college student in Finland,in 1991",
        learn_more_url="https://www.freecodecamp.org/news/linux-is-25-yay-lets-celebrate-with-25-rad-facts-about-linux-c8d8ac30076d/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the Linux penguin mascot?",
        true="Tux",
        false=["Tail", "Ping", "Flux"],
        explanation="Linux’s mascot is a penguin named “Tux”",
        learn_more_url="https://www.freecodecamp.org/news/linux-is-25-yay-lets-celebrate-with-25-rad-facts-about-linux-c8d8ac30076d/",
        difficulty=1
        ),
        QuizQuestion(
        question="In what year was the Linux Operating System created?",
        true="1991",
        false=["1990", "1989", "1992"],
        explanation="Linus Torvalds created Linux as a college student in Finland,in 1991",
        learn_more_url="https://www.freecodecamp.org/news/linux-is-25-yay-lets-celebrate-with-25-rad-facts-about-linux-c8d8ac30076d/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the cd command stand for?",
        true="change directory",
        false=["create directory", "created directory", "changed directory"],
        explanation="cd stands for change directory",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-cd-command",
        difficulty=1
        ),
        QuizQuestion(
        question="What does Bash stand for?",
        true="Bourne-again shell",
        false=["Born-again shell", "Basic shell", "Bourne-another shell"],
        explanation="All shells originate from the Bourne Shell and the name Bourne\" is used  because its creator was Steve Bourne. Bash means Bourne-again shell. ",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-cd-command",
        difficulty=1
        ),
        QuizQuestion(
        question="Which of the following is the pipe symbol in Linux?",
        true="|",
        false=["/", "\\", "[]"],
        explanation="With the pipe symbol (|), the output of one command serves as the input to another",
        learn_more_url="https://www.freecodecamp.org/news/the-linux-commands-handbook/#the-linux-cd-command",
        difficulty=1
        )
    ]

    python_questions = [

        QuizQuestion(
        question="What logical operator in Python returns True if both operands are True?",
        true="and",
        false=["or", "not", ""],
        explanation="The logical operator and returns True if both operands are True and False otherwise.",
        learn_more_url="https://www.freecodecamp.org/news/basic-operators-in-python-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What logical operator in Python returns True if any of the operands is True?",
        true="or",
        false=["and", "not", ""],
        explanation="The logical operator or returns True if any of the operands is True. ",
        learn_more_url="https://www.freecodecamp.org/news/basic-operators-in-python-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What logical operator in Python returns True if the operand is False?",
        true="not",
        false=["and", "or", ""],
        explanation="The logical operator not returns True if the operand is False and False if the operand is True.",
        learn_more_url="https://www.freecodecamp.org/news/basic-operators-in-python-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these operators is used to raise a number to the power of an exponent in Python? ",
        true="**",
        false=["*", "^", "!"],
        explanation="The power operator is ** in Python. We use it to raise the number on the left to the power of the exponent on the right. For example, 5 ** 3 means 5 raised to the power 3. The result would be 125.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-python-operators",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the “greater than” operator in Python?",
        true=">",
        false=[">=", "<", "<="],
        explanation="The “greater than” operator is > in Python. It returns True if the value on the left is greater than the value on the right. We can also use it to compare strings in alphabetical order.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-python-operators",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the “greater than or equal to” operator in Python?",
        true=">=",
        false=[">", "<", "<="],
        explanation="The “greater than or equal to” operator is >= in Python. It returns True if the value on the left is greater than or equal to the value on the right. We can also use it to compare strings in alphabetical order.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-python-operators",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the “less than” operator in Python?",
        true="<",
        false=[">", "<=", ">="],
        explanation="The “less than” operator is < in Python. It returns True if the value on the left is less than the value on the right. We can also use it to compare strings in alphabetical order.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-python-operators",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the “less than or equal to” operator in Python?",
        true="<=",
        false=["<", ">", ">="],
        explanation="The “less than or equal to” operator is <= in Python. It returns True if the value on the left is less than or equal to the value on the right. We can also use it to compare strings in alphabetical order.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-python-operators",
        difficulty=1
        ),
        QuizQuestion(
        question="What operator can you use in Python to check if a value is in a sequence?",
        true="in",
        false=["member", "inside", "partof"],
        explanation="The in operator is a membership operator in Python. It can be used to check if a value is in a sequence or not because it returns True if the value is in the list and False if it is not in the list. ",
        learn_more_url="https://www.freecodecamp.org/news/basic-operators-in-python-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What function can you use to transform a number represented as a string into an integer in Python?",
        true="int()",
        false=["float()", "complex()", "bin()"],
        explanation="The int() function takes a string as argument and returns an integer.",
        learn_more_url="https://www.freecodecamp.org/news/how-to-convert-strings-into-integers-in-python/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the data type of the value returned by the input() function in Python?",
        true="String",
        false=["Integer", "Boolean", "List"],
        explanation="The built-in function input() always returns a string. If you need to work with this value as a different data type, you will need to convert it.",
        learn_more_url="https://www.freecodecamp.org/news/python-function-guide-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you write a “Hello, World” program in Python?",
        true="print(“Hello, World!”)",
        false=["console.log(“Hello, World!”)", "show(“Hello, World!”)", "console(“Hello, World!”)"],
        explanation="In Python, we use the built-in print() function to print a value to the console. We pass the value as argument within parentheses. ",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-hello-world-program-in-python",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is {b}not{/b} a Python keyword?",
        true="forward",
        false=["if", "return", "for"],
        explanation="These three words: if, return, and for, are Python keywords but forward is not a Python keyword. Python keywords are reserved words, so they cannot be used as variable names, function names, or any other identifiers in a Python program. ",
        learn_more_url="https://forum.freecodecamp.org/t/python-keywords-a-guide-with-examples/19188",
        difficulty=2
        ),
        QuizQuestion(
        question="What operator is used in Python to concatenate strings?",
        true="+",
        false=["*", "-", "/"],
        explanation="When the operands are strings, the + operator concatenates them to create a new string. For example: “Hello” + “World” evaluates to 'HelloWorld'.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-python-operators",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is a valid variable name in Python?",
        true="my_variable_59",
        false=["59my_variable", "my^_variable", "my_variable59%"],
        explanation="Variable names in Python cannot start with a number, they must start with a letter or an underscore. They can only contain alphanumeric characters and underscores (A-Z, a-z, 0-9, and _).",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-variable-definitions-in-python",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is a valid comment in Python?",
        true="# This is a comment",
        false=["// This is a comment", "* This is a comment", "/* This is a comment */"],
        explanation="In Python, we start a comment with a hash symbol #. A line that starts with this symbol will be interpreted as a comment in a Python program. ",
        learn_more_url="https://forum.freecodecamp.org/t/how-to-comment-your-code-in-python-explained-with-examples/19220",
        difficulty=1
        ),
        QuizQuestion(
        question="What Python keyword is used to return a value from a function?",
        true="return",
        false=["pass", "continue", "break"],
        explanation="The return keyword is used to return a value from a function.This terminates the execution of the function to return the value.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-functions-in-python",
        difficulty=2
        ),
        QuizQuestion(
        question="What is the meaning of PEP in Python?",
        true="Python Enhancement Proposal",
        false=["Python Experimentation Platform", "Python Excellent Performance", "Python Environmental Protection"],
        explanation="In the context of Python, PEP means Python Enhancement Proposal. A PEP is a design document that provides information to the Python community, or describes a new feature for Python or its processes or environment.",
        learn_more_url="https://www.python.org/dev/peps/pep-0001/#what-is-a-pep",
        difficulty=3
        ),
        QuizQuestion(
        question="What value does a Python function return by default if it doesn’t have a return statement?",
        true="None",
        false=["0", "An empty string", "An empty list"],
        explanation="Python functions return the special value None if they do not have an explicit return statement.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-functions-in-python",
        difficulty=2
        ),
        QuizQuestion(
        question="What is the result of this Python code: “Hi” * 2?",
        true="“HiHi”",
        false=["“Hihi”", "“HiHiHiHi”", "A SyntaxError"],
        explanation="The * operator in Python can be used to repeat a string a given number of times. In this case, the string “Hi” is repeated two times. ",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-python-operators",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these operators has the highest precedence in Python?",
        true="**",
        false=["/", "*", "and"],
        explanation="The exponentiation operator ** has the highest precedence of these four options.",
        learn_more_url="https://docs.python.org/3/reference/expressions.html#operator-precedence",
        difficulty=2
        ),
        QuizQuestion(
        question="In Python, it is recommended to write variable names in lowercase with words separated by...",
        true="an underscore",
        false=["an asterisk", "a space", "a hash symbol"],
        explanation="PEP 8, the Style Guide for Python Code, recommends writing variable names in lowercase with words separated by an underscore as necessary to improve readability.",
        learn_more_url="https://www.python.org/dev/peps/pep-0008/#function-and-variable-names",
        difficulty=1
        ),
        QuizQuestion(
        question="In Python, strings are...",
        true="Immutable",
        false=["Mutable", "", ""],
        explanation="Strings are immutable, so we can’t update or remove their characters after they have been defined in the program. ",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-data-types-and-built-in-data-structures-in-python",
        difficulty=2
        ),
        QuizQuestion(
        question="What built-in data structure in Python can store key-value pairs? ",
        true="Dictionary",
        false=["List", "Tuple", "String"],
        explanation="A dictionary can store key-value pairs, which are pairs of associated values. We use the key to access its corresponding value in the dictionary. ",
        learn_more_url="https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/",
        difficulty=1
        ),
        QuizQuestion(
        question="What built-in Python function returns the length of a sequence?",
        true="len()",
        false=["length()", "size()", "s()"],
        explanation="The len() function returns the length (number of items) of an object.",
        learn_more_url="https://docs.python.org/3/library/functions.html#len",
        difficulty=1
        ),
        QuizQuestion(
        question="Are tuples mutable or immutable in Python?",
        true="Immutable",
        false=["Mutable", "", ""],
        explanation="Tuples are immutable built-in data structures in Python. This means that you cannot add new elements to a tuple, you cannot update existing elements and you cannot remove elements from a tuple. ",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-data-types-and-built-in-data-structures-in-python",
        difficulty=1
        ),
        QuizQuestion(
        question="Are lists mutable or immutable in Python?",
        true="Mutable",
        false=["Immutable", "", ""],
        explanation="Lists are mutable built-in data structures in Python. This means that you can add new elements to a list, update the elements of a list, and remove elements from a list.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-data-types-and-built-in-data-structures-in-python",
        difficulty=1
        ),
        QuizQuestion(
        question="How many spaces are recommended per level of indentation in Python?",
        true="4",
        false=["1", "2", "3"],
        explanation="In Python, it is recommended to use 4 spaces per level of indentation.",
        learn_more_url="https://www.python.org/dev/peps/pep-0008/#indentation",
        difficulty=1
        ),
        QuizQuestion(
        question="What do you use to create comments in Python?",
        true="#",
        false=["!", "//", "/* */"],
        explanation="Everything after the # symbol is considered a comment and therefore is not executed",
        learn_more_url="https://www.freecodecamp.org/news/the-ultimate-guide-to-python-from-beginner-to-intermediate-to-pro/#comment-",
        difficulty=1
        ),
        QuizQuestion(
        question="How does the addition assignment operator look like in Python?",
        true=" +=",
        false=[" =+", " +", " =="],
        explanation="The += operator lets you add two values together and store the result of the calculation in a variable. It is shorter than using + and then = ,separately",
        learn_more_url="https://www.freecodecamp.org/news/the-ultimate-guide-to-python-from-beginner-to-intermediate-to-pro/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which built-in function is used for receiving user input in Python?",
        true="input()",
        false=["in()", "user()", "receive()"],
        explanation="The input() function is used to take input from a user",
        learn_more_url="https://www.freecodecamp.org/news/the-ultimate-guide-to-python-from-beginner-to-intermediate-to-pro/",
        difficulty=1
        ),
        QuizQuestion(
        question="How to cast a any data type to a string in Python?",
        true="Using the str() function",
        false=["Using the int() function", "Using the string() function", "Using the integer() function"],
        explanation="The str() function  converts any type into a string type",
        learn_more_url="https://www.freecodecamp.org/news/learn-typecasting-in-python-in-five-minutes-90d42c439743/",
        difficulty=1
        ),
        QuizQuestion(
        question="What Python operator is used to check if two values are equal?",
        true="==",
        false=["=", "===", "!=="],
        explanation="The == operator is used to check if two values are equal in Python. It returns True if the values are equal and False otherwise.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-python-operators",
        difficulty=1
        ),
        QuizQuestion(
        question="The integer used to refer to a character in a string or an element in a list or tuple is known as...",
        true="index",
        false=["integer", "location", "position"],
        explanation="Strings, lists, tuples, and other sequences in Python have indices, which are integers used to refer to its elements. ",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-data-types-and-built-in-data-structures-in-python",
        difficulty=1
        ),
        QuizQuestion(
        question="In Python, the first index of a sequence is...",
        true="0",
        false=["1", "-1", "2"],
        explanation="The first index of a sequence in Python is 0.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-data-types-and-built-in-data-structures-in-python",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the new line character in Python?",
        true="\n",
        false=["\s", "\new", "\m"],
        explanation="\n is the newline character in Python.",
        learn_more_url="https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you create an empty list in Python?",
        true="[]",
        false=["dict()", "{}", "()"],
        explanation="You can create an empty list with [] or with list() in Python.",
        learn_more_url="https://www.freecodecamp.org/news/python-empty-list-tutorial-how-to-create-an-empty-list-in-python/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you create an empty set in Python?",
        true="set()",
        false=["{}", "dict()", "()"],
        explanation="You must call the set() function to create empty set in Python.",
        learn_more_url="https://www.freecodecamp.org/news/python-sets-detailed-visual-introduction/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you create an empty dictionary in Python?",
        true="{}",
        false=["[]", "()", "list()"],
        explanation="You can create an empty dictionary with {} in Python.",
        learn_more_url="https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/",
        difficulty=1
        ),
        QuizQuestion(
        question="In Python, the keys of a dictionary must be...",
        true="Immutable",
        false=["Mutable", "Both will work", ""],
        explanation="The keys of a Python dictionary must be immutable.",
        learn_more_url="https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/",
        difficulty=1
        ),
        QuizQuestion(
        question="In Python, the values of a dictionary must be...",
        true="They can be immutable or mutable",
        false=["Immutable", "Mutable", ""],
        explanation="The values of a Python dictionary can be either mutable or immutable. Both will work correctly. ",
        learn_more_url="https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/",
        difficulty=1
        ),
        QuizQuestion(
        question="If you try to access a key that does not exist in a Python dictionary, you will get a...",
        true="KeyError",
        false=["SyntaxError", "ValueError", "TypeError"],
        explanation="If you try to access a key that does not exist in a Python dictionary, you will get a KeyError.",
        learn_more_url="https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you check if the key \"Nora\" is in the \"names\" dictionary?",
        true="\"Nora\" in names",
        false=["names in \"Nora\"", "\"Nora\" is in names", "names is in \"Nora\""],
        explanation="To check if a key is in a dictionary, first we write the key followed by in and then the name of the dictionary. In this case, the correct option is \"Nora\" in names.",
        learn_more_url="https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/",
        difficulty=1
        ),
        QuizQuestion(
        question="What method adds an element to the end of a list in Python?",
        true=".append()",
        false=[".add()", ".join()", ".end()"],
        explanation="The .append() method adds an element to the end of a list in Python.",
        learn_more_url="https://www.freecodecamp.org/news/python-list-append-how-to-add-an-element-to-an-array-explained-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What method takes an iterable as argument and adds the elements of that iteable to a list as individual elements?",
        true=".extend()",
        false=[".append()", ".join()", ".add()"],
        explanation="The .extend() method takes an iterable as argument and adds the elements of that list to a list as individual elements.",
        learn_more_url="https://www.freecodecamp.org/news/python-list-append-vs-python-list-extend/",
        difficulty=1
        ),
        QuizQuestion(
        question="A value that evaluates to True in a boolean context is known as...",
        true="Truthy",
        false=["TRUE", "Falsy", "Truthful"],
        explanation="A value that evaluates to True in a boolean context is known as a truthy value.",
        learn_more_url="https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/",
        difficulty=2
        ),
        QuizQuestion(
        question="A value that evaluates to False in a boolean context is known as...",
        true="Falsy",
        false=["FALSE", "Truth", "Truthy"],
        explanation="A value that evaluates to False in a boolean context is known as a falsy value.",
        learn_more_url="https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/",
        difficulty=2
        ),
        QuizQuestion(
        question="Empty sequences, collections and the number 0 are...",
        true="Falsy",
        false=["Truthy", "", ""],
        explanation="Empty sequences, collections, and the number 0 are falsy values in Python.",
        learn_more_url="https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/",
        difficulty=1
        ),
        QuizQuestion(
        question="Non-empty sequences, non-empty collections, and numerical values different from 0 are...",
        true="Truthy",
        false=["Falsy", "", ""],
        explanation="Non-empty sequences, collections, and numerical values different from 0 are truthy values.",
        learn_more_url="https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/",
        difficulty=1
        ),
        QuizQuestion(
        question="Exception raised in Python when you try to index a list, tuple, or string beyond the permitted boundaries.",
        true="IndexError",
        false=["KeyError", "NameError", "TypeError"],
        explanation="An IndexError is raised in Python when you try to index a list, tuple, or string beyond the permitted boundaries.",
        learn_more_url="https://www.freecodecamp.org/news/exception-handling-python/",
        difficulty=2
        ),
        QuizQuestion(
        question="Exception raised in Python when you try to access the value of a key that doesn't exist in a dictionary.",
        true="KeyError",
        false=["IndexError", "NameError", "TypeError"],
        explanation="A KeyError is raised in Python when you try to access the value of a key that doesn't exist in a dictionary.",
        learn_more_url="https://www.freecodecamp.org/news/exception-handling-python/",
        difficulty=2
        ),
        QuizQuestion(
        question="Exception raised in Python when a name that you are referencing in the code doesn't exist.",
        true="NameError",
        false=["KeyError", "IndexError", "TypeError"],
        explanation="A NameError is raised in Python when a name that you are referencing in the code doesn't exist.",
        learn_more_url="https://www.freecodecamp.org/news/exception-handling-python/",
        difficulty=2
        ),
        QuizQuestion(
        question="Exception raised in Python when an operation or function is applied to an object of an inappropriate type. ",
        true="TypeError",
        false=["NameError", "KeyError", "IndexError"],
        explanation="A TypeError is raised in Python when an operation or function is applied to an object of an inappropriate type. ",
        learn_more_url="https://www.freecodecamp.org/news/exception-handling-python/",
        difficulty=2
        ),
        QuizQuestion(
        question="Exception raised in Python when you try to divide by zero.",
        true="ZeroDivisionError",
        false=["TypeError", "NameError", "KeyError"],
        explanation="A ZeroDivisionError is raised in Python when you try to divide by zero.",
        learn_more_url="https://www.freecodecamp.org/news/exception-handling-python/",
        difficulty=2
        ),
        QuizQuestion(
        question="What method is used to remove a key-value pair from a dictionary in Python and return its value?",
        true=".pop()",
        false=[".push()", ".append()", ".insert()"],
        explanation="The .pop() method is used to remove a key-value pair from the dictionary and return the value.",
        learn_more_url="https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/",
        difficulty=1
        ),
        QuizQuestion(
        question="What function can you call to open a file in Python?",
        true="open()",
        false=["read()", "extend()", "print()"],
        explanation="The open() function opens a file in a Python program. ",
        learn_more_url="https://www.freecodecamp.org/news/python-write-to-file-open-read-append-and-other-file-handling-functions-explained/",
        difficulty=2
        ),
        QuizQuestion(
        question="What built-in Python function allows you to iterate over multiple iterables in parallel by returning a tuple with an item from each one?",
        true="zip()",
        false=["iterate()", "print()", "range()"],
        explanation="The zip() function allows you to iterate over multiple iterables in parallel by returning a tuple with an item from each one.",
        learn_more_url="https://www.freecodecamp.org/news/the-zip-function-in-python-explained-with-examples/",
        difficulty=2
        ),
        QuizQuestion(
        question="What built-in Python function returns the smallest item in an iterable or the smallest of two or more arguments?",
        true="min()",
        false=["max()", "minimum()", "smallest)"],
        explanation="The min() function returns the smallest item in an iterable or the smallest of two or more arguments.",
        learn_more_url="https://www.freecodecamp.org/news/python-function-guide-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What built-in Python function returns the largest item in an iterable or the largest of two or more arguments?",
        true="max()",
        false=["min()", "maximum()", "largest()"],
        explanation="The max() function returns the largest item in an iterable or the largest of two or more arguments.",
        learn_more_url="https://www.freecodecamp.org/news/python-function-guide-with-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What built-in Python function returns a new sorted list from the items in an iterable?",
        true="sorted()",
        false=["sort()", "print()", "copy()"],
        explanation="The sorted() function returns a new sorted list from the items in an iterable. ",
        learn_more_url="https://www.freecodecamp.org/news/python-sort-list-how-to-order-by-descending-or-ascending/",
        difficulty=1
        ),
        QuizQuestion(
        question="What built-in Python function returns a reverse iterator that allows you to iterate over the elements of an iterable in reverse order?",
        true="reverse()",
        false=["sorted()", "reversed()", "backwards()"],
        explanation="The reversed() function returns a reverse iterator that you can use to iterate over an iterable in reverse order.",
        learn_more_url="https://docs.python.org/3/library/functions.html#reversed",
        difficulty=1
        ),
        QuizQuestion(
        question="What built-in Python function returns a number rounded to a given number of digits of precision after the decimal point?",
        true="round()",
        false=["rounded()", "approximate()", "decimal()"],
        explanation="The round() function returns a number rounded to a given number of digits of precision after the decimal point.",
        learn_more_url="https://docs.python.org/3/library/functions.html#round",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you define a variable in Python?",
        true="<variable_name> = <value>",
        false=["<value> = <variable_name>", "<value> <= <variable_name>", "<variable_name> <= <value>"],
        explanation="In Python, we define a variable with <variable_name> = <value>.",
        learn_more_url="https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/",
        difficulty=1
        )
    ]

    sql_questions = [

        QuizQuestion(
        question="What is SQL?",
        true="A language used for relational databases",
        false=["A language that translates code from one languages to another", "A language that converts data into machine code", "A language used for non relational databases"],
        explanation="SQL is used to store, manipulate and retrieve data in relational database management systems. ",
        learn_more_url="https://www.freecodecamp.org/news/learn-sql-in-10-minutes/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does SQL stand for?",
        true="Structured Query Language",
        false=["Standardized Question Language", "String Query Language", "Single Query Language"],
        explanation="SQL stands for Structured Query Language and it is used with relational databases.",
        learn_more_url="https://www.freecodecamp.org/news/learn-sql-in-10-minutes/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which database system DOES NOT use the SQL syntax?",
        true="MongoDB",
        false=["MySQL", "PostgreSQL", "Microsoft SQL Server"],
        explanation="Popular database systems that use SQL syntax are MySQL, PostgreSQL, Microsoft SQL Server, and SQLite. (Note(Oliver): it seems odd list rdbms when we're talking about mongo)",
        learn_more_url="https://www.freecodecamp.org/news/learn-sql-in-10-minutes/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT a type of data model used in NoSQL?",
        true="Infix notation",
        false=["key-value", "document", "wide-column or tabular"],
        explanation="NoSQL supports a variety of data models including  'key-value', 'document', 'wide-column or tabular' formats",
        learn_more_url="https://www.freecodecamp.org/news/learn-nosql-in-3-hours/",
        difficulty=1
        ),
        QuizQuestion(
        question="A structured set of data stored in a computer designed for efficient storage, retrieval, and maintenance is known as...",
        true="Database",
        false=["Dataset", "Query", "Table"],
        explanation="A database is a structured set of data stored in a computer designed for efficient storage, retrieval, and maintenance.",
        learn_more_url="https://www.freecodecamp.org/news/sql-and-databases-explained-in-plain-english/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does DBMS stand for?",
        true="Database Management System",
        false=["Dataset Management System", "Database Maintenance System", "Database Management Site"],
        explanation="DBMS stands for Database Management System. ",
        learn_more_url="https://www.freecodecamp.org/news/sql-and-databases-explained-in-plain-english/",
        difficulty=1
        ),
        QuizQuestion(
        question="The values of a table are known as...",
        true="Fields",
        false=["API", "Query", "Database"],
        explanation="The values of a table are known as fields.",
        learn_more_url="https://www.freecodecamp.org/news/sql-and-databases-explained-in-plain-english/",
        difficulty=1
        ),
        QuizQuestion(
        question="An individual entry in a table of a database is known as...",
        true="Record/Row",
        false=["Column", "Cell", "Query"],
        explanation="An individual entry in a table of a database is known as record or row.",
        learn_more_url="https://www.freecodecamp.org/news/sql-and-databases-explained-in-plain-english/",
        difficulty=1
        ),
        QuizQuestion(
        question="Part of a SQL query that determines which columns of data to show in the results.",
        true="SELECT",
        false=["TABLE", "CREATE", "QUERY"],
        explanation="SELECT determines which columns will be shown in the result.",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the SQL command to create a table?",
        true="CREATE TABLE <table-name>",
        false=["TABLE CREATE <table-name>", "NEW TABLE <table-name>", "TABLE NEW <table-name>"],
        explanation="CREATE TABLE <table-name> is the SQL command to create a table with this name. ",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=1
        ),
        QuizQuestion(
        question="The column or set of columns that uniquely identifies each row in a table is known as...",
        true="Primary Key",
        false=["Secondary Key", "First Key", "Foreign Key"],
        explanation="The primary key is the column or set of columns that uniquely identify a row. ",
        learn_more_url="https://www.freecodecamp.org/news/the-sql-primary-key-constraint-explained/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the SQL command used to order the results in ascending or descending order?",
        true="ORDER BY",
        false=["SORT BY", "ASCENDING", "DESCENDING"],
        explanation="The ORDER BY command is used in SQL to sort the results in ascending or descending order.",
        learn_more_url="https://www.freecodecamp.org/news/sql-and-databases-explained-in-plain-english/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the SQL command used to change the structure of a table?",
        true="ALTER TABLE",
        false=["CHANGE TABLE", "UPDATE TABLE", "MODIFY TABLE"],
        explanation="The ALTER TABLE command is used to change the structure of a table in SQL.",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the constraint used in SQL to limit the range of values that can be placed in a column?",
        true="CHECK",
        false=["RANGE", "RESTRICT", "VALIDATE"],
        explanation="The CHECK constraint is used to limit the range of values that can be placed in a column.",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=1
        ),
        QuizQuestion(
        question="What SQL clause is used to limit the number of rows returned by a query based on specific criteria?",
        true="WHERE",
        false=["LIMIT", "FILTER", "CHECK"],
        explanation="The WHERE clause is used in SQL to limit the number of rows returned based on specific criteria.",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=1
        ),
        QuizQuestion(
        question="What SQL statement is used to update a record in a table?",
        true="UPDATE",
        false=["CHANGE", "SELECT", "QUERY"],
        explanation="The UPDATE statement is used to update the value of a record in SQL.",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=1
        ),
        QuizQuestion(
        question="What SQL statement is used to combine groups and aggregate data?",
        true="GROUP BY",
        false=["UPDATE", "CLASSIFY", "CATEGORY"],
        explanation="The GROUP BY statement is used to combine rows and aggregate data.",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=1
        ),
        QuizQuestion(
        question="What SQL command allows you to rename a column or table using an alias?",
        true="AS",
        false=["ALIAS", "SET", "NAME"],
        explanation="The AS command is used to rename a column or table using an alias.",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=1
        ),
        QuizQuestion(
        question="Normalized databases are optimized to reduce...",
        true="Data redundancy",
        false=["Read time", "Query size", "Storage space"],
        explanation="Normalized databases are optimized to reduce data redundancy.",
        learn_more_url="https://www.freecodecamp.org/news/sql-and-databases-explained-in-plain-english/",
        difficulty=2
        ),
        QuizQuestion(
        question="A computer programming language used to inserting, deleting, and updating data in a database is known as...",
        true="Data Manipulation Language",
        false=["Data Definition Language", "Data Control Language", ""],
        explanation="A computer programming language used to inserting, deleting, and updating data in a database is known as Data Manipulation Language.",
        learn_more_url="https://en.wikipedia.org/wiki/Data_manipulation_language",
        difficulty=2
        ),
        QuizQuestion(
        question="What does DDL stand for?",
        true="Data Definition Language",
        false=["Data Manipulation Language", "Data Control Language", ""],
        explanation="DDL stands for Data Definition Language. ",
        learn_more_url="https://en.wikipedia.org/wiki/Data_definition_language",
        difficulty=2
        ),
        QuizQuestion(
        question="What does DML stand for?",
        true="Data Manipulation Language",
        false=["Data Definition Language", "Data Control Language", ""],
        explanation="DML stands for Data Manipulation Language.",
        learn_more_url="https://en.wikipedia.org/wiki/Data_manipulation_language",
        difficulty=2
        ),
        QuizQuestion(
        question="What does DCL stand for?",
        true="Data Control Language",
        false=["Data Manipulation Language", "Data Definition Language", ""],
        explanation="DCL stands for Data Control Language.",
        learn_more_url="https://en.wikipedia.org/wiki/Data_control_language",
        difficulty=2
        ),
        QuizQuestion(
        question="What SQL command allows you to filter the data aggregated by the GROUP BY clause so that the user gets a limited set of records to view?",
        true="HAVING",
        false=["FILTER", "QUERY", "SELECT"],
        explanation="The HAVING command allows you to filter the data aggregated by the GROUP BY clause so that the user gets a limited set of records to view.",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=2
        ),
        QuizQuestion(
        question="What aggregate function in SQL allows you to calculate the average of a numeric column from the set of rows returned by a query?",
        true="AVG()",
        false=["COUNT()", "MINIMUM()", "AVERAGE()"],
        explanation="The AVG() function is used to calculate the average of a column from the set of rows returned by a query.",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=2
        ),
        QuizQuestion(
        question="What aggregate function in SQL allows you to count the number of rows and return that count as a column in the result set?",
        true="COUNT()",
        false=["AVG()", "MINIMUM()", "AVERAGE()"],
        explanation="The COUNT() function is used to count the number of rows and return that count as a column in the result set",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=2
        ),
        QuizQuestion(
        question="What type of join in SQL returns all rows for which there is a match in either of the tables?",
        true="FULL OUTER JOIN",
        false=["RIGHT OUTER JOIN", "LEFT OUTER JOIN", "INNER JOIN"],
        explanation="A FULL OUTER JOIN returns all rows for which there is a match in either of the tables.",
        learn_more_url="https://www.freecodecamp.org/news/basic-sql-commands/",
        difficulty=2
        ),
        QuizQuestion(
        question="What type of join in SQL returns rows that have a match in both tables?",
        true="INNER JOIN",
        false=["FULL OUTER JOIN", "RIGHT OUTER JOIN", "LEFT OUTER JOIN"],
        explanation="A INNER JOIN returns all rows for which there is a match in both tables.",
        learn_more_url="https://www.freecodecamp.org/news/the-ultimate-guide-to-sql-join-statements/",
        difficulty=2
        ),
        QuizQuestion(
        question="What type of join in SQL returns all the records from the left table and the matched records from the right table?",
        true="LEFT OUTER JOIN",
        false=["FULL OUTER JOIN", "INNER JOIN", "RIGHT OUTER JOIN"],
        explanation="A LEFT OUTER JOIN returns all the records from the left table and the matched records from the right table.",
        learn_more_url="https://www.freecodecamp.org/news/the-ultimate-guide-to-sql-join-statements/",
        difficulty=2
        ),
        QuizQuestion(
        question="What type of join in SQL returns all the records from the right table and the matched records from the left table?",
        true="RIGHT OUTER JOIN",
        false=["LEFT OUTER JOIN", "FULL OUTER JOIN", "INNER JOIN"],
        explanation="A RIGHT OUTER JOIN returns all the records from the right table and the matched records from the left table.",
        learn_more_url="https://www.freecodecamp.org/news/the-ultimate-guide-to-sql-join-statements/",
        difficulty=2
        )
    ]