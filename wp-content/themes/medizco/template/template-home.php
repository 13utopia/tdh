<?php
/**
 * template-home.php
 *
 * Template Name: Home Page Template
 * Template Post Type: page
 */

get_header();
?>

<div id="post-<?php the_ID(); ?>" <?php post_class('home-page-contents');?> role="main">
  <div class="builder-content">
    <?php
    while ( have_posts() ) : the_post();
      the_content();
    endwhile;
    ?>
  </div><!-- .builder-content -->
</div><!-- .home-page-contents -->

<?php
get_footer();
