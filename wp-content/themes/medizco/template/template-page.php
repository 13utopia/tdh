<?php
/**
 * template-page.php
 *
 * Template Name: Page Template
 * Template Post Type: page, medizco-doctor, medizco-service
 */

get_header();
if('medizco-service' == get_post_type()){
    get_template_part( 'template-parts/banner/content', 'banner-service' );
}else{
    get_template_part( 'template-parts/banner/content', 'banner-page' );
}
?>

<div id="post-<?php the_ID(); ?>" <?php post_class('page-contents');?> role="main">
  <div class="builder-content">
    <?php
    while ( have_posts() ) : the_post();
      the_content();
    endwhile;
    ?>
  </div><!-- .builder-content -->
</div><!-- .page-contents -->

<?php
get_footer();
