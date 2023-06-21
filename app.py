import streamlit as st
from instaloader import Instaloader, Profile




def main():
    st.title("Instagram Statistics")
    username = st.text_input("Enter Instagram username:")
    if st.button("Get Statistics"):
        stats = get_instagram_stats(username)
        st.subheader(f"Username: {stats['username']}")
        st.write(f"Posts: {stats['posts']}")
        st.write(f"Followers: {stats['followers']}")
        st.write(f"Engagement Rate: {stats['engagement_rate']:.2f}%")
        st.write(f"Estimated Reach: {stats['estimated_reach']:.2f}")
        st.write(f"Total Likes: {stats['total_likes']}")
        st.write(f"Total Comments: {stats['total_comments']}")
        st.write(f"Potential Impact: {stats['potential_impact']}")
        st.write(f"Potential Reach: {stats['potential_reach']}")
        st.write(f"Influence: {stats['influence']}")
        st.write(f"Average Likes per Post: {stats['average_likes_per_post']:.2f}")
        
        st.subheader("Top Posts:")
        for i, post in enumerate(stats['top_posts']):
            st.write(f"\nPost {i+1}:")
            st.write(f"URL: {post['url']}")
            st.write(f"Likes: {post['likes']}")
            st.write(f"Comments: {post['comments']}")

if __name__ == '__main__':
    main()
