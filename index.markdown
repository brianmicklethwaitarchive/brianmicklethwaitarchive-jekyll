---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

Welcome to the Brian Micklethwait Archive. We are slowly adding
writings to this site. For progress on this see the [news](news.html)
section.

{% include generated_quotes.html %}

## Archives

- [About Brian](aboutbrian/)
- [Libertarian Alliance Pamphlets](la/)
- [Blog Highlights](blog-highlights.html)

## Latest Update

{% for post in site.categories.news limit:1 %}
[{{ post.title }}]({{ post.url }})

{{ post.content }}
{% endfor %}

## Highlight

In this video, [Steve Baker MP](https://www.stevebaker.info/) recounts how Brian introduced him to books about freedom.

<iframe width="560" height="315" src="https://www.youtube.com/embed/gKB0Xt0hIQ8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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
- [Brian's library](https://www.libib.com/u/sjgibbs/l/1303003)

### Video
- [Channel 4 Documentary](https://youtu.be/Hhmog-5plwo?t=1384): 'If I were Prime Minister' with Chris Tame
- [Internet Archive videos](https://archive.org/details/@libertarian_videos)
- [YouTube search results](https://www.youtube.com/results?search_query=brian+micklethwait)
