---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

Welcome to the Brian Micklethwait Archive. We have started to add
writings to this site. For progress on this see the [news](news.html)
section.

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
    content: '\201C';
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
        <li class="anim1">
          <div class="testimonial-quote group">
            <div class="quote-container">
	      <blockquote>
	        <p>Only strongly and consistently held opinions get media coverage, because only those who strongly mean what they are saying can spare all that time and trouble to assemble appropriate clutches of The Facts to decorate their opinions and get the media to pay attention.</p>
              </blockquote>  
              <cite><span><a href="/la/histn022.html">The Tyranny of Facts</a></span><br>
                1990
              </cite>
            </div>
          </div>
        </li>
        <li class="anim2">
          <div class="testimonial-quote group">
            <div class="quote-container">
              <blockquote>
                <p>If a Philistine is someone who despises a square of canvas painted to look like the bottom of a rubbish skip, then I glory in the title.</p>
              </blockquote>
	      <cite><span><a href="/la/cultn002.html">Against Art Subsidies</a></span><br>
                1983
              </cite>
            </div>
	  </div>
        </li>
        <li class="anim3">
          <div class="testimonial-quote group">
            <div class="quote-container">
              <blockquote>
                <p>Not only is success largely in the mind. The really good news is that we can control our minds, what we think about, what we imagine, what we tell ourselves, what we <b>feel</b>.</p>
              </blockquote>  
              <cite><span><a href="/la/psycn007.html">What the Success Books Say</a></span><br>
                1992
              </cite>
            </div>
	  </div>
        </li>
        <li class="anim4">
          <div class="testimonial-quote group">
            <div class="quote-container">
              <blockquote>
	        <p>Not for the first time in the history of human conflict, an overwhelmingly superior force delayed the obliteration of its far weaker enemy, on the grounds that this could as easily be done later rather than sooner, and that in the meantime there was some fun to be had.</p>
              </blockquote>  
              <cite><span><a href="/la/lific001.html">Those Who Can Do</a></span><br>
                1996
              </cite>
            </div>
	  </div>
        </li>
        <li class="anim5">
          <div class="testimonial-quote group">
            <div class="quote-container">
              <blockquote>
	        <p>The famous Manhattan skyline is a sky line because land values vary continuously rather than discontinuously, not because any one person ever drew that line.</p>
              </blockquote>  
              <cite><span><a href="/la/cultn003.html">Freedom, Order and Architecture</a></span><br>
                1983
              </cite>
            </div>
	  </div>
        </li>
      </ul>
    </div>
  </div>
</div>


## Latest Update

{% for post in site.posts limit:1 %}
[{{ post.title }}]({{ post.url }})

{{ post.content }}
{% endfor %}

## Archives

[Libertarian Alliance Pamphlets](la/)

## Elsewhere

Here is a collection of other places
on the internet where you may find writings by Brian.

- [Brian Micklethwait's New Blog](https://www.brianmicklethwaitsnewblog.com/)
- [Contributions to Samizdata](https://www.samizdata.net/author/brian/)
- [Podcasts with Patrick Crozier](https://croziervision.podbean.com/)
- [Old blog](http://www.brianmicklethwait.com/)
- [Culture blog](http://www.brianmicklethwait.com/culture/archives/2003/01/)
- [Education blog](http://www.brianmicklethwait.com/index.php/education)
- [Libertarian Alliance pamphlets](http://www.libertarian.co.uk/lapubs/pubindex.htm)
- [Normblog profile](https://normblog.typepad.com/normblog/2007/02/the_normblog_pr_2.html)

### Video
- [Channel 4 Documentary](https://youtu.be/Hhmog-5plwo?t=1384): 'If I were Prime Minister' with Chris Tame
- [Internet Archive videos](https://archive.org/details/@libertarian_videos)
- [YouTube search results](https://www.youtube.com/results?search_query=brian+micklethwait)
