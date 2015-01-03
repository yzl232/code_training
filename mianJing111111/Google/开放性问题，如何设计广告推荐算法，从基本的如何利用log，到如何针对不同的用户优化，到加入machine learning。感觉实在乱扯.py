# encoding=utf-8
'''
开放性问题，如何设计广告推荐算法，从基本的如何利用log，到如何针对不同的用户优化，到加入machine learning。感觉实在乱扯
'''


'''


It is both an art and a science. Typical fields of study revolve around market basket analysis (also called affinity analysis) which is a subset of the field of data mining. Typical components in such a system include identification of primary driver items and the identification of affinity items (accessory upsell, cross sell).

Keep in mind the data sources they have to mine...

    Purchased shopping carts = real money from real people spent on real items = powerful data and a lot of it.
    Items added to carts but abandoned.
    Pricing experiments online (A/B testing, etc.) where they offer the same products at different prices and see the results
    Packaging experiments (A/B testing, etc.) where they offer different products in different "bundles" or discount various pairings of items
    Wishlists - what's on them specifically for you - and in aggregate it can be treated similarly to another stream of basket analysis data
    Referral sites (identification of where you came in from can hint other items of interest)
    Dwell times (how long before you click back and pick a different item)
    Ratings by you or those in your social network/buying circles - if you rate things you like you get more of what you like and if you confirm with the "i already own it" button they create a very complete profile of you
    Demographic information (your shipping address, etc.) - they know what is popular in your general area for your kids, yourself, your spouse, etc.
    user segmentation = did you buy 3 books in separate months for a toddler? likely have a kid or more.. etc.
    Direct marketing click through data - did you get an email from them and click through? They know which email it was and what you clicked through on and whether you bought it as a result.
    Click paths in session - what did you view regardless of whether it went in your cart
    Number of times viewed an item before final purchase
    If you're dealing with a brick and mortar store they might have your physical purchase history to go off of as well (i.e. toys r us or something that is online and also a physical store)
    etc. etc. etc.

Luckily people behave similarly in aggregate so the more they know about the buying population at large the better they know what will and won't sell and with every transaction and every rating/wishlist add/browse they know how to more personally tailor recommendations. Keep in mind this is likely only a small sample of the full set of influences of what ends up in recommendations, etc.

Now I have no inside knowledge of how Amazon does business (never worked there) and all I'm doing is talking about classical approaches to the problem of online commerce - I used to be the PM who worked on data mining and analytics for the Microsoft product called Commerce Server. We shipped in Commerce Server the tools that allowed people to build sites with similar capabilities.... but the bigger the sales volume the better the data the better the model - and Amazon is BIG. I can only imagine how fun it is to play with models with that much data in a commerce driven site. Now many of those algorithms (like the predictor that started out in commerce server) have moved on to live directly within Microsoft SQL.

The four big take-a-ways you should have are:

    Amazon (or any retailer) is looking at aggregate data for tons of transactions and tons of people... this allows them to even recommend pretty well for anonymous users on their site.
    Amazon (or any sophisticated retailer) is keeping track of behavior and purchases of anyone that is logged in and using that to further refine on top of the mass aggregate data.
    Often there is a means of over riding the accumulated data and taking "editorial" control of suggestions for product managers of specific lines (like some person who owns the 'digital cameras' vertical or the 'romance novels' vertical or similar) where they truly are experts
    There are often promotional deals (i.e. sony or panasonic or nikon or canon or sprint or verizon pays additional money to the retailer, or gives a better discount at larger quantities or other things in those lines) that will cause certain "suggestions" to rise to the top more often than others - there is always some reasonable business logic and business reason behind this targeted at making more on each transaction or reducing wholesale costs, etc.

In terms of actual implementation? Just about all large online systems boil down to some set of pipelines (or a filter pattern implementation or a workflow, etc. you call it what you will) that allow for a context to be evaluated by a series of modules that apply some form of business logic.

Typically a different pipeline would be associated with each separate task on the page - you might have one that does recommended "packages/upsells" (i.e. buy this with the item you're looking at) and one that does "alternatives" (i.e. buy this instead of the thing you're looking at) and another that pulls items most closely related from your wish list (by product category or similar).

The results of these pipelines are able to be placed on various parts of the page (above the scroll bar, below the scroll, on the left, on the right, different fonts, different size images, etc.) and tested to see which perform best. Since you're using nice easy to plug and play modules that define the business logic for these pipelines you end up with the moral equivalent of lego blocks that make it easy to pick and choose from the business logic you want applied when you build another pipeline which allows faster innovation, more experimentation, and in the end higher profits.

Did that help at all? Hope that give you a little bit of insight how this works in general for just about any ecommerce site - not just Amazon. Amazon (from talking to friends that have worked there) is very data driven and continually measures the effectiveness of it's user experience and the pricing, promotion, packaging, etc. - they are a very sophisticated retailer online and are likely at the leading edge of a lot of the algorithms they use to optimize profit - and those are likely proprietary secrets (you know like the formula to KFC's secret spices) and guaarded as such.

'''

# 于是乎

'''
Recommender systems typically produce a list of recommendations in one of two ways - through collaborative or content-based filtering.[5] Collaborative filtering approaches building a model from a user's past behavior (items previously purchased or selected and/or numerical ratings given to those items) as well as similar decisions made by other users; then use that model to predict items (or ratings for items) that the user may have an interest in.[6] Content-based filtering approaches utilize a series of discrete characteristics of an item in order to recommend additional items with similar properties.[7] These approaches are often combined (see Hybrid Recommender Systems).

The differences between collaborative and content-based filtering can be demonstrated by comparing two popular music recommender systems - Last.fm and Pandora Radio.

    Pandora uses the properties of a song or artist (a subset of the 400 attributes provided by the Music Genome Project) in order to seed a "station" that plays music with similar properties. User feedback is used to refine the station's results, deemphasizing certain attributes when a user "dislikes" a particular song and emphasizing other attributes when a user "likes" a song. This is an example of a content-based approach.
    Last.fm creates a "station" of recommended songs by observing what bands and individual tracks that the user has listened to on a regular basis and comparing those against the listening behavior of other users. Last.fm will play tracks that do not appear in the user's library, but are often played by other users with similar interests. As this approach leverages the behavior of users, it is an example of a collaborative filtering technique.

Each type of system has its own strengths and weaknesses. In the above example, Last.fm requires a large amount of information on a user in order to make accurate recommendations. This is an example of the cold start problem, and is common in collaborative filtering systems.[8] While Pandora needs very little information to get started, it is far more limited in scope (for example, it can only make recommendations that are similar to the original seed).
'''