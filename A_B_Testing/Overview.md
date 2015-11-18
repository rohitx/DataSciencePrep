# A/B Testing

## Overview of A/B Testing

A/B Testing allows you to determine scientifically how to optimize a website by trying out various changes and seeing what works best. Using A/B test means you get data to make decisions rather than relying on intuition.

For example:

* Google tested 41 different shades of blue.
* Amazon initially decided to launch their first personalized product recommendations based on an A/B test showing a huge revenue increase by adding that feature. (See the second paragraph in the introduction.)
* LinkedIn tested whether to use the top slot on a user's stream for top news articles or an encouragement to add more contacts. (See the first paragraph in "A/B testing with view based JSON" section.)
* Amazon determined that every 100ms increase in page load time decreased sales by 1%. (In "Secondary metrics" section on the last page)
Google’s latency results showed a similar impact for a 100ms delay.

What are some of the things you cannot do with A/B testing? A/B testing will not work in the following scenarios:

1. Testing without a hypothesis. When you devise an A/B test you need to figure out what the hypothesis should be. This is because the A/B test is here to make your hypothesis confirmed or refuted. Most often when designing an A/B test, you should look into the details about what the consumers want and create your hypothesis based on it. Without hypothesis, doing an A/B test is like flipping a coin.
2. Comparing more than one thing. When working with A/B it is extremely important to only change one thing at a time. Changing too many things at the same time can affect the result and therefore the hypothesis.
3. Campaigns are a great way to create awareness of the actual service or product and increase web traffic and conversion rate. However, in campaigns the users often come to site to check out rather than purchase anything. This decreases the chances of them buying anything and hence reduces the conversion rate. If you are A/B testing you want to ensure that this does not happen as it skews the result.
4. A/B testing cannot tell you if you are missing anything on the website or any of the product that you use to A/B test. It only tells us whether one is better than the other.

What is A/B testing?

A/B testing is an experiment where you have set of buckets: the controlled set and the experimental set. Suppose you want to test which version of the website is better. So the control set will have the old version and the experimental set will have the new version. You are then going to find how users react different to these two groups in order to find which version is more effective.

When can you use A/B testing?

* You can use it when you want to test a premium service where people need to register and pay in order to get more content. But this will provide you to gather information but you will not be able to fully test it.
* See if a new movie algorithm that you have created to recommend movies works
* Change the backend in order to improve load time, results users see, etc...
* Suppose you want to design a website to sell cars. You want to see will a change increase repeat customers or referrals? Note that in case of referrals the test will take too long to determine. This is because referrals and returning customers to buy a car takes too long. So because the length of the time is so long, you will not be able to A/B test.
* Update brand, including main logo. This may look like a good idea however, changing logo can make users emotional. You can only do the A/B test on a changed logo if the users have gotten used to the change.
* Test layout of an initial page. This is a good example of an A/B test as there are clear control and metrics to evaluate.

A/B testing is much like hypothesis testing where you have a controlled group and an experiment group. In the same manner you want to design A/B test that will give you similar result in case of repeated tests.

### Example

Let's look at an example. We have an education website called audacity.com. We want to create a 'Start Now' button on the main page to take the user to the second page. We want to decide whether the color of this button should be orange or pink. In order to know how decide which color is most effective, we carry out an A/B test. However, what is the metric we should choose? Here are some possibilities:

* We could choose the total number of courses completed. But this will take too long as students may take anywhere from weeks to months.
* We could look at the number of clicks. However, there is a problem with this. Say in Group 1 more people viewed the page but only 2 clicked. In Group 2, two people viewed the page and 1 clicked. So we see that there were greater percentage of clicks in Group 2 than Group 1. So, which one is better? So, instead of looking at just clicks we look at the fraction of page visitors who clicked. This is given by the number of clicks / number of page views which is also known as **click-through-rate**.
* The other metric to use is called **click-through-probability**. It is defined as the unique visitors who click / unique visitors to page.

Here's how the metric works: Suppose two people, Alexis and Carmen visit the page. Alexis sees page 1 and does not click while the Carmen sees new page 1 and clicks 5 times. In this case the Alexis has CTR of 0 and Carmen has 5. However, the probabilities are: 5/2 = 2.5 for Alexis and 1/2 = 0.5 for Carmen.

From this we can conclude that changing the "Start Now" button from orange to pink will increase the click-through-probability of the button.

You use CTR when you want to measure the usability of the site and CTP when you want to measure the total impact of the site. For example you want to know how effective is a button on your site (where there can be many buttons), you would use the CTR. When you want to know how often the users went to the second level of the website, you use the CTP.

When it comes to CTR or CTP, we use the binomial distribution. This is because the clicks are not continuous. We can that the in the binomial distribution the click is a success and no click is a failure.

