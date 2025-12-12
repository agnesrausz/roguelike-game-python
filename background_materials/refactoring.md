# Refactoring

Let's see the usage of clean code principles through a real-life example of refactoring.

_"The @author field of a Javadoc tells us who we are. We are authors. And one thing about authors is that they have
readers. Indeed, authors are responsible for communicating well with their readers. The next time you write a line of
code, remember you are an author, writing for readers who will judge your effort."
_ *(from 'Clean code' by Robert C. Martin)*

Uncle Bob (alias Robert C. Martin) states in his famous book *Clean code* that spending time and energy for writing
self-explaining and readable code pays off as we *read* code way more than *write*.

You might experience in the last few weeks that it could be challenging to overlook and understand the code of even a
2-week-long project. So imagine the code of a 1-, 2- or even 10-year-long project. Scary, isn't it?

Good news is that there are practices both for keep the code quality and to refactor to clean code.

## Steps of refactoring code

Here are some steps that can help you to make the code clean.

- Read through the whole code

- Summarize what is the purpose of the script in one sentence.

- Run the code to see what is the end result

- The code should keep runnable and show the same content when you finish the refactor

- Do not forget to run the code frequently to check you are on the right track

How to refactor it?
Remove clutter: Clutter is anything in your code that does not add value

- Format your code

- Delete comments

Remove complexity:

- bad names

- long methods

- deep conditionals

- improper variable scopes (global, local)

- Remove cleverness: If it's simple and elegant you wouldn't refer to it as 'clever'

Remove duplication:

- This can be applied by extracting the duplicated code parts into functions

## Refactoring in action

To see the whole process with an explanation in action watch the video below.

The video is quite long, but mentors of former classes reported that the ones who watched it has significantly deeper
understanding about refactoring and clean code.

The video touches advanced topics (tests, classes, coupling, etc.). Just ignore them and concentrate on the main
principles, aspects and the process of refactoring.

### C# version

[![Play on YouTube](https://img.youtube.com/vi/aWiwDdx_rdo/0.jpg)](https://www.youtube.com/watch?v=aWiwDdx_rdo)

### Java version

[![Play on YouTube](https://img.youtube.com/vi/Zfgc7qJEZZ0/0.jpg)](https://www.youtube.com/watch?v=Zfgc7qJEZZ0)
