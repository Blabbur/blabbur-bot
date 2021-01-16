import sgqlc.types


schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

ID = sgqlc.types.ID

Int = sgqlc.types.Int

String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################

########################################################################
# Output Objects and Interfaces
########################################################################
class AuthPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('token', 'user')
    token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='token')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class Comment(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'text', 'tweet', 'user', 'is_comment_mine', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    tweet = sgqlc.types.Field('Tweet', graphql_name='tweet')
    user = sgqlc.types.Field('User', graphql_name='user')
    is_comment_mine = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCommentMine')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')


class File(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'tweet', 'user')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    tweet = sgqlc.types.Field('Tweet', graphql_name='tweet')
    user = sgqlc.types.Field('User', graphql_name='user')


class Like(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'tweet', 'user')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    tweet = sgqlc.types.Field('Tweet', graphql_name='tweet')
    user = sgqlc.types.Field('User', graphql_name='user')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('add_comment', 'delete_comment', 'toggle_like', 'delete_tweet', 'new_tweet', 'toggle_retweet', 'update_tweet', 'edit_profile', 'follow', 'login', 'signup', 'unfollow')
    add_comment = sgqlc.types.Field(sgqlc.types.non_null(Comment), graphql_name='addComment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='text', default=None)),
))
    )
    delete_comment = sgqlc.types.Field(sgqlc.types.non_null(Comment), graphql_name='deleteComment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    toggle_like = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='toggleLike', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_tweet = sgqlc.types.Field('Tweet', graphql_name='deleteTweet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    new_tweet = sgqlc.types.Field(sgqlc.types.non_null('Tweet'), graphql_name='newTweet', args=sgqlc.types.ArgDict((
        ('text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='text', default=None)),
        ('files', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='files', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags', default=None)),
))
    )
    toggle_retweet = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='toggleRetweet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_tweet = sgqlc.types.Field('Tweet', graphql_name='updateTweet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='text', default=None)),
))
    )
    edit_profile = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='editProfile', args=sgqlc.types.ArgDict((
        ('firstname', sgqlc.types.Arg(String, graphql_name='firstname', default=None)),
        ('lastname', sgqlc.types.Arg(String, graphql_name='lastname', default=None)),
        ('bio', sgqlc.types.Arg(String, graphql_name='bio', default=None)),
        ('website', sgqlc.types.Arg(String, graphql_name='website', default=None)),
        ('dob', sgqlc.types.Arg(String, graphql_name='dob', default=None)),
        ('avatar', sgqlc.types.Arg(String, graphql_name='avatar', default=None)),
        ('cover_photo', sgqlc.types.Arg(String, graphql_name='coverPhoto', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
))
    )
    follow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='follow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    login = sgqlc.types.Field(sgqlc.types.non_null(AuthPayload), graphql_name='login', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
))
    )
    signup = sgqlc.types.Field(sgqlc.types.non_null(AuthPayload), graphql_name='signup', args=sgqlc.types.ArgDict((
        ('firstname', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='firstname', default=None)),
        ('lastname', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='lastname', default=None)),
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
        ('handle', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='handle', default=None)),
))
    )
    unfollow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unfollow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('search_by_tag', 'search_by_tweet', 'tweet', 'feed', 'me', 'profile', 'search_by_user', 'users')
    search_by_tag = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tweet'))), graphql_name='searchByTag', args=sgqlc.types.ArgDict((
        ('term', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='term', default=None)),
))
    )
    search_by_tweet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tweet'))), graphql_name='searchByTweet', args=sgqlc.types.ArgDict((
        ('term', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='term', default=None)),
))
    )
    tweet = sgqlc.types.Field(sgqlc.types.non_null('Tweet'), graphql_name='tweet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    feed = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tweet'))), graphql_name='feed')
    me = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='me')
    profile = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='profile', args=sgqlc.types.ArgDict((
        ('handle', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='handle', default=None)),
))
    )
    search_by_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='searchByUser', args=sgqlc.types.ArgDict((
        ('term', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='term', default=None)),
))
    )
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='users')


class Retweet(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'tweet', 'user', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    tweet = sgqlc.types.Field('Tweet', graphql_name='tweet')
    user = sgqlc.types.Field('User', graphql_name='user')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='updatedAt')


class Tweet(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'user', 'text', 'tags', 'files', 'comments', 'likes', 'retweets', 'likes_count', 'comments_count', 'retweets_count', 'is_liked', 'is_tweet_mine', 'is_retweet', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field('User', graphql_name='user')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags')
    files = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='files')
    comments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Comment))), graphql_name='comments')
    likes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Like))), graphql_name='likes')
    retweets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Retweet))), graphql_name='retweets')
    likes_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='likesCount')
    comments_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='commentsCount')
    retweets_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='retweetsCount')
    is_liked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLiked')
    is_tweet_mine = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTweetMine')
    is_retweet = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRetweet')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')


class User(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'firstname', 'lastname', 'handle', 'email', 'cover_photo', 'avatar', 'bio', 'location', 'website', 'dob', 'tweets', 'retweets', 'following', 'followers', 'comments', 'likes', 'files', 'fullname', 'is_self', 'is_following', 'following_count', 'followers_count', 'tweets_count', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    firstname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstname')
    lastname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastname')
    handle = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='handle')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    cover_photo = sgqlc.types.Field(String, graphql_name='coverPhoto')
    avatar = sgqlc.types.Field(String, graphql_name='avatar')
    bio = sgqlc.types.Field(String, graphql_name='bio')
    location = sgqlc.types.Field(String, graphql_name='location')
    website = sgqlc.types.Field(String, graphql_name='website')
    dob = sgqlc.types.Field(String, graphql_name='dob')
    tweets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Tweet))), graphql_name='tweets')
    retweets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Retweet))), graphql_name='retweets')
    following = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='following')
    followers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='followers')
    comments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Comment))), graphql_name='comments')
    likes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Like))), graphql_name='likes')
    files = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='files')
    fullname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullname')
    is_self = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSelf')
    is_following = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFollowing')
    following_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='followingCount')
    followers_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='followersCount')
    tweets_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tweetsCount')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

