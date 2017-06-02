################################################################################
# Stats screen.
#
# This displays RPG-like statistics.
################################################################################

default player_hp = 15
default player_hp_max = 42
default eileen_hp = 100
default eileen_hp_max = 100

default player_lv = 4
default eileen_lv = 99

# This screen displays a single stat.
screen single_stat(name, hp, hp_max, lv, xalign):

    frame:
        xalign xalign

        vbox:
            spacing 5

            hbox:
                text "[name]" min_width 220
                text _(" Lv. [lv]")

            hbox:
                text "HP":
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(hp, hp_max, 1.0)
                    xmaximum 180
                    ysize 26


                text " [hp]/[hp_max]":
                    yalign 0.5


# This screen uses single_stat to display two stats at once.
screen stats():
    use single_stat(_("Player"), player_hp, player_hp_max, player_lv, 0.0)
    use single_stat(_("Eileen"), eileen_hp, eileen_hp_max, eileen_lv, 1.0)


################################################################################
# Day picker
#
# This code displays a day picker, including statistics and a way of choosing
# an action for each period of the day.
################################################################################


# This constant defines the periods in the day.
define day_periods = [ _('Morning'), _('Afternoon'), _('Evening') ]

# This constant defines what to do in each period.
define day_choices = [ _('Study'), _('Exercise'), _('Eat'), _('Drink'), _('Be Merry') ]

# This is a dictionary mapping a period to a
default day_plan = {
    'Morning' : 'Eat',
    'Afternoon' : 'Drink',
    'Evening' : 'Be Merry'
    }

# These variables display statistics to the player.
default stat_strength = 10
default stat_intelligence = 25
default stat_moxie = 100
default stat_chutzpah = 75

# These styles are used to style the various stats.
style stat_text is default:
    min_width 150
    text_align 1.0
    yalign 0.5

style stat_hbox is hbox:
    spacing 10

style stat_vbox:
    spacing 5


# This is the day planner screen. It displays the

screen day_planner():

    # This vbox organizes everything.
    vbox:

        spacing 5

        # A frame containing all the stats.
        frame:
            style_prefix "stat"
            xpadding 150
            xfill True

            vbox:

                hbox:
                    text _("Strength")
                    bar value StaticValue(stat_strength, 100)

                hbox:
                    text _("Intelligence")
                    bar value StaticValue(stat_strength, 100)

                hbox:
                    text _("Moxie")
                    bar value StaticValue(stat_strength, 100)

                hbox:
                    text _("Chutzpah")
                    bar value StaticValue(stat_strength, 100)


        # A grid of three frames, one for each of the periods in the day.
        grid 3 1:

            spacing 5
            xfill True

            for p in day_periods:

                frame:
                    xfill True

                    vbox:
                        label p

                        null height 5

                        for i in day_choices:
                            textbutton i action SetDict(day_plan, p, i)

        # This is a grid containing two empty space and the done button,
        # so everything lines up.
        grid 3 1:
            xfill True
            spacing 5

            null

            frame:
                textbutton "Done":
                    action Return(True)
                    xfill True

                    text_xalign 0.5

            null





label tutorial_screens:

    e "Screens are the most powerful part of Ren'Py. Screens let you customize the out-of-game interface, and create new in-game interface components."

label screens_menu:

    $ reset_example()

    menu:

        e "What would you like to know about screens?"

        "What can screens do?":
            call screens_demo

        "How to show screens.":
            call screens_showing

        "Passing parameters to screens.":
            call screens_parameters

        "Screen properties.":
            call screens_properties

        "That's it.":
            return

    jump screens_menu


label screens_demo:

    e "Screens are how we create the user interface in Ren'Py. With the exception of images and transitions, everything you see comes from a screen."

    e "When I'm speaking to you, I'm using the 'say' screen. It's responsible for taking dialogue and presenting it to the player."

    menu:

        e "And when the menu statement displays an in-game choice, the 'choice' screen is used. Got it?"

        "Yes.":
            pass

        "I do.":
            pass

    e "Text input uses the 'input' screen, NVL mode uses the 'nvl' screen, and so on."

    e "More than one screen can be displayed at once. For example, the buttons at the bottom - Back, History, Skip, and so on - are all displayed by a quick_menu screen that's shown all of the time."

    e "There are a lot of special screens, like 'main_menu', 'load', 'save', and 'preferences'. Rather than list them all here, I'll {a=https://www.renpy.org/doc/html/screen_special.html}send you to the documentation{/a}."

    e "In a newly created project, all these screens live in screens.rpy. You can edit that file in order to change them."

    e "You aren't limited to these screens either. In Ren'Py, you can make your own screens, and use them for your game's interface."

    $ player_hp = 15

    show screen stats
    with dissolve

    e "For example, in an RPG like visual novel, a screen can display the player's statistics."

    $ player_hp = 42

    e "Which reminds me, I should probably heal you."

    hide screen stats
    show screen day_planner

    with dissolve

    e "Complex screens can be the basis of whole game mechanics. A stats screen like this can be the basis of dating and life-sims."

    hide screen day_planner
    with dissolve

    e "While screens might be complex, they're really just the result of a lot of simple parts working together to make something larger than all of them."

    return




label screens_showing:

    example large:
        screen simple_screen():
            frame:
                xalign 0.5 ypos 50
                vbox:
                    text "This is a screen."
                    textbutton "Okay":
                        action Return(True)


    e "Here's an example of a very simple screen. The screen statement is used to tell Ren'Py this is a screen, and it's name is simple_screen."

    e "Inside the screen statement, lines introduces displayables such as frame, vbox, text, and textbutton; or properties like action, xalign, and ypos."

    show screen simple_screen

    e "I'll work from the inside out to describe the statements. But first, I'll show the screen so you can see it in action."

    e "The text statement is used to display the text provided."

    e "The textbutton statement introduces a button that can be clicked. When the button is clicked, the provided action is run."

    e "Both are inside a vbox, which means vertical box, statement - that places the text on top of the button."

    e "And that is inside a frame that provides the background and borders. The frame has an at property that takes a transform giving its position."

    hide screen simple_screen
    hide screen example

    e "There are a trio of statements that are used to display screens."

    example:
        show screen simple_screen

        e "The first is the show screen statement, which displays a screen and lets Ren'Py keep going."

        e "The screen will stay shown until it is hidden."

        hide screen simple_screen

        e "Hiding a screen is done with the hide screen statement."

    show example call_screen

    e "The call screen statement stops Ren'Py from executing script until the screen either returns a value, or jumps the script somewhere else."

    e "Since we can't display dialogue at the same time, you'll have to click 'Okay' to continue."

    hide example
    window hide

    example call_screen hide:
        call screen simple_screen

    e "When a call screen statement ends, the screen is automatically hidden."

    e "Generally, you use show screen to show overlays that are up all the time, and call screen to show screens the player interacts with for a little while."

    return


label screens_parameters():



















label imagemap_tutorial:

    show example imagemap

    e "Another type of screen is an imagemap. An imagemap uses images that display hotspots that act as buttons."

    e "This imagemap uses two images - one when a button is idle, and one when a button is hovered. The idle image also doubles as a background."

    e "When a player clicks on a hotspot, this imagemap runs a Jump action to take them to a label. Each hotspots also has alt text, for vision-impared players."

    hide example

    e "Let's take a look at an imagemap screen in action."

    jump imagemap_example

example imagemap hide:
    screen imagemap_example:

        imagemap:
            ground "imagemap ground"
            hover "imagemap hover"

            hotspot (44, 238, 93, 93) action Jump("swimming") alt "Swimming"
            hotspot (360, 62, 93, 93) action Jump("science") alt "Science"
            hotspot (726, 106, 93, 93) action Jump("art") alt "Art"
            hotspot (934, 461, 93, 93) action Jump("go home") alt "Go Home"

    label imagemap_example:

        # Call the imagemap_example screen.
        call screen imagemap_example

    label swimming:

        e "You chose swimming."

        e "Swimming seems like a lot of fun, but I didn't bring my bathing suit with me."

        jump imagemap_done

    label science:

        e "You chose science."

        e "I've heard that some schools have a competitive science team, but to me research is something that can't be rushed."

        jump imagemap_done

    label art:
        e "You chose art."

        e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

        jump imagemap_done

    label home:

        e "You chose to go home."

        jump imagemap_done

    label imagemap_done:

        e "Anyway..."

label after_imagemap_example:

    show screen stats
    with dissolve

    e "Screens can do a lot. For example, if a game is an RPG - or even RPG-themed - we can display statistics to the player."

    hide screen stats
    with dissolve

    window show

    $ e("For a dating sim or life simulation game, we can display scheduling interfaces like this one.", interact=False)
    call screen day_planner

    e "Screens can also be used to customize all parts of the Ren'Py interface - for example, the say screen is what shows dialogue to the player."

    e "Screens might look complicated, and more complex ones can have a lot of code in them. But every screen is made out of lots of small parts."

    return