---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

Welcome to the Brian Micklethwait Archive. We have started to add
writings to this site. For progress on this see the [news](news.html)
section.

{% include generated_quotes.html %}

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
