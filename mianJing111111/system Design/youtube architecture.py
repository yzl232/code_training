# encoding=utf-8
'''
http://highscalability.com/youtube-architecture
# http://highscalability.com/blog/2012/3/26/7-years-of-youtube-scalability-lessons-in-30-minutes.html
'''




'''
 Most popular content is moved to a CDN (content delivery network):
- CDNs replicate content in multiple places. There's a better chance of content being closer to the user, with fewer hops, and content will run over a more friendly network.
- CDN machines mostly serve out of memory because the content is so popular there's little thrashing of content into and out of memory.
Less popular content (1-20 views per day) uses YouTube servers in various colo sites.
- There's a long tail effect. A video may have a few plays, but lots of videos are being played. Random disks blocks are being accessed.
- Caching doesn't do a lot of good in this scenario, so spending money on more cache may not make sense. This is a very interesting point. If you have a long tail product caching won't always be your performance savior.
- Tune RAID controller and pay attention to other lower level issues to help.
- Tune memory on each machine so there's not too much and not too little.
'''