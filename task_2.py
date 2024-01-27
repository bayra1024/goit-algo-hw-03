import turtle


def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)


def draw_complete_snowflake(turtle, order, size):
    for _ in range(3):
        koch_snowflake(turtle, order, size)
        turtle.right(120)


def main():
    order = int(input("Введіть рівень рекурсії (ціле число): "))

    screen = turtle.Screen()
    screen.bgcolor("#2b353a")
    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)
    snowflake_turtle.color("#82f701")

    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()

    start_pos = snowflake_turtle.pos()
    draw_complete_snowflake(snowflake_turtle, order, order * 180)
    end_pos = snowflake_turtle.pos()
    snowflake_turtle.penup()
    snowflake_turtle.goto(start_pos)
    snowflake_turtle.pendown()
    snowflake_turtle.goto(end_pos)

    screen.exitonclick()


if __name__ == "__main__":
    main()
