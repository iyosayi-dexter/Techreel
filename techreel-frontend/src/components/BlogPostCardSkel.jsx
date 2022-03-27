import Shimmer from './SkelShimmer'

const BlogPostCardSkel = () => {
    return (
        <main className='skeleton_containter skel_blogPostCard'>
            <div className='skeleton skel_blogPostImage'/>
            <section className='skeleton_wrapper skel_blogPostTags'>
                <div className='skeleton skel_blogPostTag'></div>
                <div className='skeleton skel_blogPostTag'></div>
                <div className='skeleton skel_blogPostTag'></div>
            </section>
            <div className='skeleton skel_blogPostText'/>
            <div className='skeleton skel_blogPostExert'/>
            <Shimmer/>
        </main>
    )
}
export default BlogPostCardSkel

export const TextSkel=()=>{
    return (
        <div className='skeleton_containter skel_contain'>
            <div className='skeleton skel_bigText'/>
            <Shimmer/>
        </div>
    )
}

