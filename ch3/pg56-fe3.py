# The Empire State Building is 102 stories high. A man wanted to know
# the highest floor from which he could drop an egg without the egg
# breaking. He proposed to drop the egg from the top floor. If it broke,
# he would go down a floor, and try it again. He would do this until the
# egg did not break. At worse this method would require 102 eggs. Implement
# a method that at worse uses seven eggs.

# egg drop bisection method

stories = 102
eggs = 1
print(stories)
while stories > 1:
    if True:
        stories = stories//2
        print(stories)
        eggs += 1
print('Eggs used:', eggs)
