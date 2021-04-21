import yaml
import random
import sys


first_quote_should_contain = sys.argv[1] if len(sys.argv) > 1 else None

quotes_prefix = """
<!-- Carousel by Cassidy Williams: https://codepen.io/cassidoo/pen/MyaWzp -->
<!-- Blockquotes by Andrew Wright: https://codepen.io/andrewwright/pen/Aigre -->

<style type="text/css">
.content-slider {
  width: 100%;
  height: 360px;
}

.slider {
  height: 320px;
  margin: 40px auto 0;
  overflow: visible;
  position: relative;
}

.mask {
  overflow: hidden;
  height: 320px;
}

.slider ul {
  margin: 0;
  padding: 0;
  position: relative;
}

.slider li {
  height: 320px;
  position: absolute;
  top: -325px;
  list-style: none;
}

.slider .quote {
  font-size: 40px;
  font-style: italic;
}

.slider .source {
  font-size: 20px;
  text-align: right;
}

.slider li.anim1 {
  animation: cycle 90s linear infinite;
}

.slider li.anim2 {
  animation: cycle2 90s linear infinite;
}

.slider li.anim3 {
  animation: cycle3 90s linear infinite;
}

.slider li.anim4 {
  animation: cycle4 90s linear infinite;
}

.slider li.anim5 {
  animation: cycle5 90s linear infinite;
}

.slider:hover li {
  animation-play-state: paused;
}

@keyframes cycle {
  0% {
    top: 0px;
  }
  4% {
    top: 0px;
  }
  16% {
    top: 0px;
    opacity: 1;
    z-index: 0;
  }
  20% {
    top: 325px;
    opacity: 0;
    z-index: 0;
  }
  21% {
    top: -325px;
    opacity: 0;
    z-index: -1;
  }
  50% {
    top: -325px;
    opacity: 0;
    z-index: -1;
  }
  92% {
    top: -325px;
    opacity: 0;
    z-index: 0;
  }
  96% {
    top: -325px;
    opacity: 0;
  }
  100% {
    top: 0px;
    opacity: 1;
  }
}

@keyframes cycle2 {
  0% {
    top: -325px;
    opacity: 0;
  }
  16% {
    top: -325px;
    opacity: 0;
  }
  20% {
    top: 0px;
    opacity: 1;
  }
  24% {
    top: 0px;
    opacity: 1;
  }
  36% {
    top: 0px;
    opacity: 1;
    z-index: 0;
  }
  40% {
    top: 325px;
    opacity: 0;
    z-index: 0;
  }
  41% {
    top: -325px;
    opacity: 0;
    z-index: -1;
  }
  100% {
    top: -325px;
    opacity: 0;
    z-index: -1;
  }
}

@keyframes cycle3 {
  0% {
    top: -325px;
    opacity: 0;
  }
  36% {
    top: -325px;
    opacity: 0;
  }
  40% {
    top: 0px;
    opacity: 1;
  }
  44% {
    top: 0px;
    opacity: 1;
  }
  56% {
    top: 0px;
    opacity: 1;
    z-index: 0;
  }
  60% {
    top: 325px;
    opacity: 0;
    z-index: 0;
  }
  61% {
    top: -325px;
    opacity: 0;
    z-index: -1;
  }
  100% {
    top: -325px;
    opacity: 0;
    z-index: -1;
  }
}

@keyframes cycle4 {
  0% {
    top: -325px;
    opacity: 0;
  }
  56% {
    top: -325px;
    opacity: 0;
  }
  60% {
    top: 0px;
    opacity: 1;
  }
  64% {
    top: 0px;
    opacity: 1;
  }
  76% {
    top: 0px;
    opacity: 1;
    z-index: 0;
  }
  80% {
    top: 325px;
    opacity: 0;
    z-index: 0;
  }
  81% {
    top: -325px;
    opacity: 0;
    z-index: -1;
  }
  100% {
    top: -325px;
    opacity: 0;
    z-index: -1;
  }
}

@keyframes cycle5 {
  0% {
    top: -325px;
    opacity: 0;
  }
  76% {
    top: -325px;
    opacity: 0;
  }
  80% {
    top: 0px;
    opacity: 1;
  }
  84% {
    top: 0px;
    opacity: 1;
  }
  96% {
    top: 0px;
    opacity: 1;
    z-index: 0;
  }
  100% {
    top: 325px;
    opacity: 0;
    z-index: 0;
  }
}

.testimonial-quote {
    font-size: 14px;
}

.testimonial-quote blockquote {
    /* Negate theme styles */
    border: 0;
    margin: 0;
    padding: 0;

    background: none;
    color: gray;
    font-family: Georgia, serif;
    font-size: 1.5em;
    font-style: italic;
    line-height: 1.4 !important;
    margin: 0;
    position: relative;
    text-shadow: 0 1px white;
    z-index: 600;
}

.testimonial-quote blockquote * {
    box-sizing: border-box;
}

.testimonial-quote blockquote p {
    color: #75808a;
    line-height: 1.4 !important;
}

.testimonial-quote blockquote p:first-child:before {
    content: '\\201C';
    color: #81bedb;
    font-size: 7.5em;
    font-weight: 700;
    opacity: .3;
    position: absolute;
    top: -.4em;
    left: -.2em;
    text-shadow: none;
    z-index: -300;
}

.testimonial-quote cite {
    color: gray;
    display: block;
    font-size: .8em;
}

.testimonial-quote cite span {
    color: #5e5e5e;
    font-size: 1em;
    font-style: normal;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-shadow: 0 1px white;
}

.testimonial-quote {
    position: relative;
}

.testimonial-quote .quote-container {
    padding-left: 20px;
    padding-right: 20px;
    padding-top: 16px;
}

.testimonial-quote.right cite {
    text-align: right;
}
</style>

<div class="content-slider">
  <div class="slider">
    <div class="mask">
      <ul>
"""

quotes_postfix = """
      </ul>
    </div>
  </div>
</div>
"""


with open('quotes.yml', 'r') as stream:
    quotes = yaml.safe_load(stream)
    num_quotes = len(quotes)
    quote_indexes = list(range(num_quotes))
    random.shuffle(quote_indexes)
    quotes_required = 5
    titles_used = set()
    i = 0
    max_quote_length = 400
    print(quotes_prefix)
    while len(titles_used) < quotes_required and i < num_quotes:
        # get a random quote
        quote = quotes[quote_indexes[i]]
        while first_quote_should_contain is not None:
            if first_quote_should_contain not in quote['title']:
                random.shuffle(quote_indexes)
                quote = quotes[quote_indexes[i]]
            else:
                first_quote_should_contain = None
        i += 1

        # make sure it will fit
        if len(quote['text']) <= max_quote_length and quote['title'] not in titles_used:
            titles_used.add(quote['title'])
            print(f"""
<li class="anim{len(titles_used)}">
    <div class="testimonial-quote group">
    <div class="quote-container">
    <blockquote><p>{quote['text']}</p></blockquote>
        <cite><span><a href="{quote['link']}">{quote['title']}</a></span><br>
        {quote['date']}
        </cite>
    </div>
    </div>
</li>
            """
            )
    print(quotes_postfix)
