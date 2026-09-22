<?php

$blog_author = medizco_option('blog_author');
$blog_author_name = get_the_author();
$blog_author_url = get_the_author_meta( 'user_url' );
$blog_author_bio = get_the_author_meta( 'user_description' );

?> 
<?php if ( $blog_author_bio && $blog_author == "yes" ): ?>
<div class="author-box">
    <div class="author-img pull-left">
       <?php echo get_avatar( get_the_ID() );  ?>
    </div>
    <div class="author-info">
        <h3><?php echo esc_html( $blog_author_name ); ?></h3>
        <p class="author-url">
            <a href="<?php echo esc_url( $blog_author_url ); ?>"><?php echo esc_url( $blog_author_url ); ?></a>
        </p>
        <p> 
            <?php echo esc_html( $blog_author_bio );; ?>
        </p>
     </div>
</div> <!-- Author box end -->
<?php endif; ?>
