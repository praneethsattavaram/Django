from django.shortcuts import render

# Create your views here.


articles = [
    {
        'id' : 1,
        'name' : '7 Ways to Retain More of Every Book You Read',
        'desc' : ''' Whenever you learn a new mental model or idea, it’s like the “software” in your brain gets updated. Suddenly, you can run all of your old data points through a new program. You can learn new lessons from old moments. As Patrick O’Shaughnessy says, “Reading changes the past.'''
    },
    
    
    {
        'id' : 2,
        'name' : 'When the 80/20 Rule Fails: The Downside of Being Effective',
        'desc' : '''Audrey Hepburn was an icon.

Rising to fame in the 1950s, she was one of the greatest actresses of her era. In 1953, Hepburn became the first actress to win an Academy Award, a Golden Globe Award, and a BAFTA Award for a single performance: her leading role in the romantic comedy Roman Holiday.

Even today, over half a century later, she remains one of just 15 people to earn an “EGOT” by winning all four major entertainment awards: Emmy, Grammy, Oscar, and Tony. By the 1960s, she was averaging more than one new film per year and, by everyone’s estimation, she was on a trajectory to be a movie star for decades to come.'''
    },
    
    
    {
        'id' : 3,
        'name' : 'For a More Creative Brain Follow These 5 Steps',
        'desc' : '''Nearly all great ideas follow a similar creative process and this article explains how this process works. Understanding this is important because creative thinking is one of the most useful skills you can possess. Nearly every problem you face in work and in life can benefit from innovative solutions, lateral thinking, and creative ideas.

Anyone can learn to be creative by using these five steps. That’s not to say being creative is easy. Uncovering your creative genius requires courage and tons of practice. However, this five-step approach should help demystify the creative process and illuminate the path to more innovative thinking.'''
    }
]

def base(request):
    return render(request, 'base.html')


# def home(request):
    
#     search = request.GET.get('search')
#     result = articles
    
#     if search:
#         # result = [
#         #     i for i in result
#         #         if search.lower() in i['name'].lower()
#         #     # else 
#         # ]
#         filtered_result = [
#             i for i in result
#             if search.lower() in i['name'].lower()
#         ]
        
#         # If no articles match the search, return all articles
#         result = filtered_result if filtered_result else articles

  
    # context = {
    #     'title' : 'Home Page',
    #     'search' : search,
    #     'articles' : result,
    # }
    
    # return render(request, 'articles/home.html', context)
    
    
def home(request):
    search = request.GET.get('search')
    result = articles
    no_results = False

    if search:
        
        filtered_result = [
            i for i in result
            if search.lower() in i['name'].lower()
        ]
                
        if not filtered_result:
            no_results = True
            result = articles 
        else:
            result = filtered_result

    context = {
        'title': 'Home Page',
        'search': search,
        'articles': result,
        'no_results': no_results,
    }

    return render(request, 'articles/home.html', context)



def article(request, id):
    
    for article in articles:
        if article['id'] == id:
            article_ = article
            
    context = {
        'article1' : article_
    }
    
    return render(request, 'articles/task.html', context)


def about(request):
    context = {
        'title' : 'About Page',
    }
    return render(request, 'articles/about.html', context)

def contact(request):
    context = {
        'title' : 'Contact Page',
    }
    return render(request, 'articles/contact.html', context)
