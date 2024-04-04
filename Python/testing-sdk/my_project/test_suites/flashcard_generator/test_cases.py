import dataclasses
from typing import List

from autoblocks.testing.models import BaseTestCase
from autoblocks.testing.util import md5


@dataclasses.dataclass
class TestCase(BaseTestCase):
    notes: str

    def hash(self) -> str:
        """
        This hash serves as a unique identifier for a test case throughout its lifetime.
        """
        return md5(self.notes)


def gen_test_cases() -> List[TestCase]:
    return [
        TestCase(
            notes="""Bio 101 Notes
Cells n stuff
Cells are like, the smallest thingies that are alive.
Some old dude named Hooke found them in 1665 by looking at cork.
2 kinds: Prokaryotic (no nucleus, think bacteria) & Eukaryotic (has a nucleus, like us and plants).
Cell Theory (important!!)
Everything alive = made of cells.
Cells = life's basic unit.
New cells come from old ones.
Parts of a Cell (the bits and pieces)
Cell Membrane: kinda like a bouncer, decides what gets in and out.
Nucleus: boss of the cell, has all the DNA.
Mitochondria: power station, makes energy.
Ribosomes: tiny factories for making proteins.
ER stuff:
Rough ER has ribosomes, makes proteins.
Smooth ER is like, no ribosomes, makes fats.
Golgi Thingy: packages proteins.
Lysosomes: trash disposals for cells.
Plants have extra stuff:
Chloroplasts for catching sunlight.
Cell Wall for extra toughness.
Membrane and Moving Stuff
Phospholipid bilayer = fancy term for the cell membrane structure.
It's picky about what it lets in/out.
Doing Things (Cellular Processes)
Photosynthesis: Only in plants, turns sunlight to food.
Breathing in Cells (Respiration): Turning food & O2 into energy.
Cell Division: Mitosis (for growing and fixing) & Meiosis (making baby cells).
DNA & Genes
DNA = double helix thing, basically the recipe book for making you.
Genes = specific recipes for traits like eye color.
Evolution (Darwin’s big idea)
Survival of the fittest.
Animals change over time to become better at surviving.
Random Notes:
Need to remember: Cell wall = plants only.
Mitochondria and chloroplasts have their own DNA?? Check this.
DNA to protein = transcription and translation (need to clarify).
Why does rough ER look bumpy under a microscope? Oh, because of ribosomes.
Evolution examples for exam?""",
        ),
        TestCase(
            notes="""Eng Lit Notes
Random Stuff on Books & Authors
Shakespeare (Big Deal)

Wrote plays and sonnets.
Old English (hard to read lol).
Famous stuff: "Romeo & Juliet", "Hamlet", "Macbeth".
Themes: love, power, betrayal, the supernatural.
Chaucer’s "Canterbury Tales"

Super old stories, like medieval road trip.
Different people telling tales, some funny, some serious.
Middle English (even harder to read).
American Lit Bits

Mark Twain: "Huckleberry Finn" = kid on a raft, talks about racism, freedom.
F. Scott Fitzgerald: "The Great Gatsby", 1920s jazz age, American Dream is kinda questioned.
Poetry Stuff
Poems = lots of feelings in few words.
Rhyme, rhythm, metaphors.
Emily Dickinson: Weird punctuation, lots of dashes, wrote about death and nature.
Robert Frost: "The Road Not Taken", about choices and life paths.
Modern Stuff (Kinda)
"To Kill a Mockingbird" by Harper Lee: Racism, growing up, the South.
"1984" by George Orwell: Creepy government watching everyone.
"The Catcher in the Rye" by J.D. Salinger: Teen angst, rebellion.
Themes & Symbols
Symbols: Stuff in books that stands for other stuff. Like, a road in a poem might not just be a road.
Themes: Big ideas in a story. Freedom, identity, conflict, etc.
Notes to Self:
Shakespeare invented a ton of words, look up some.
Need examples of irony from "The Great Gatsby".
What the heck is iambic pentameter again?
Look up what "postmodernism" means.
Remember to find quotes for essay on "Mockingbird".
Random Thoughts:
Why do all old books have to be tragic?
Need to watch some Shakespeare adaptations to get it better.
Symbols in "The Great Gatsby"? Green light = dream??
Is every old poem about death or what?"""
        ),
        TestCase(
            notes="""Early Stuff
Stonehenge: Big rocks in a circle, super old, no one knows why they did it.
Romans: Came, saw, conquered. Left a bunch of baths and walls (Hadrian's Wall).
Medieval Mayhem
1066: Normans (French guys) invade, William the Conqueror becomes king.
Magna Carta (1215): King John forced to sign it, basically "Kings can't do whatever they want."
Wars & Plagues
100 Years War: England vs. France, forever fighting.
Black Death: Wipes out like half the population. Seriously bad.
Tudor Drama
Henry VIII: Marries a bunch of women, starts his own church (Church of England) because the Pope won't let him divorce.
Elizabeth I: Virgin Queen, beats the Spanish Armada, arts and theatre flourish (Shakespeare time).
Civil War & The Commonwealth
1642-1651: Civil War, Charles I loses his head, literally.
Oliver Cromwell: Becomes "Lord Protector", basically a dictator but not called a king.
Restoration to Revolution
1660: Monarchy's back with Charles II.
1688: Glorious Revolution, William of Orange takes over, more power to Parliament.
Industrial Revolution
18th-19th Century: Everything changes, factories everywhere, British Empire expands big time.
20th Century Stuff
WWI & WWII: Major world wars, lots of impact.
Decolonization: Empire shrinks, countries gain independence.
Modern Bits
EU & Brexit: Joining and leaving the European Union.
Monarchs: From Elizabeth II to Charles III, royal family drama continues.
Random Thoughts:
Why so many Henrys and Edwards?
Need to remember dates for exams (ugh).
The industrial revolution = coal, steam, and smog.
How did Britain end up ruling so much of the world?"""
        ),
    ]
