
<?php if ( has_post_thumbnail() && !post_password_required() ) : ?>
		<div class="post-media post-image">
               <?php echo wp_get_attachment_image(get_post_thumbnail_id($post->ID), 'full', false, array(
                  'class' => 'img-fluid',
                  'alt'   => get_the_title()
                  )); 
               ?>
               <?php 
                  $date_style = medizco_option('blog_date_style','classic');
                  if ( $date_style == "creative" ) :
                        medizco_post_meta_date();
                  endif;
                ?>
      </div>
    
	<?php endif; ?>
	<div class="post-body clearfix">

		<!-- Article header -->
		<header class="entry-header clearfix">
			<?php medizco_post_meta(); ?>

		</header><!-- header end -->

		<!-- Article content -->
		<div class="entry-content clearfix">
			<?php
			if ( is_search() ) {
				the_excerpt();
			} else {
				the_content( esc_html__( 'Continue reading &rarr;', 'medizco' ) );
				medizco_link_pages();
			}
			?>
         <div class="post-footer clearfix">
            <?php get_template_part( 'template-parts/blog/post-parts/part', 'tags' ); ?>
         </div> <!-- .entry-footer -->
			
         <?php
            if ( is_user_logged_in() && is_single() ) {
         ?>

                  <p style="float:left;margin-top:20px;">
                  <?php
                  edit_post_link( 
                     esc_html__( 'Edit', 'medizco' ), 
                     '<span class="meta-edit">', 
                     '</span>'
                  );
                  ?>
            
           </p>
         <?php
            }
         ?>
		</div> <!-- end entry-content -->
   </div> <!-- end post-body -->
