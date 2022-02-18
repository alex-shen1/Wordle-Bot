# Wordle Bot (name TBD)

Everyone knows what Wordle is at this point, but if you don't it's a basic word game that is now operated by the New York Times [here](https://www.nytimes.com/games/wordle/index.html).

## How it works
*(TODO: write explanation)*

## Notes on performance

As you might expect, the bot does exceptionally well for narrowing down the last few letter choices, but struggles to come up with good suggestions in the early game simply due to how many possible letter combinations there are. Additionally, while a skilled human player can use logic to deduce answers within only a few guesses, the brute-force nature of the bot's method makes it so that while winning is all but guaranteed eventually, it will usually take 3-4 guesses at least to narrow down the letters.

Another note: the bot picks letters deterministially from a list sorted by frequency of letters. However, this isn't exactly how real words work (vowels tend to be on the higher end of the list, but most words are not only vowels) so it's not entirely clear whether or not this methodology is sound.


## Future Plans?

Converting this into a browser extension that automatically overlays Wordle might be interesting, maybe it'll be a hackathon project at some point. Wordle is probably gonna be irrelevant by the time I get around to doing it, though.

In any case, the NYT implementation of the game has each row as a `<game-row>` HTML element that has 5 `<game-tile>` elements corresponding to each letter. Each has the `evaluation` attribute, which _seems_ to determine what color the square becomes -— `correct` is green, `present` is yellow, and `absent` is gray. Porting this bot's Python code to JS and then writing a way to read the HTML attributes should be roughly enough to get this to work, if only just by logging recommended guesses in the console.