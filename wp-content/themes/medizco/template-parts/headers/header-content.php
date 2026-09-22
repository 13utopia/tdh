<?php
   $class = '';
   $title = 'On Social:';
   $social_title = '';
   if ( defined( 'FW' ) ) { 
      //Page settings
      $default_class = '';
      $general_main_logo      = medizco_option('general_main_logo');
   } else {
      $noquota = '';
      $default_class = 'header_default';
   }

   $site_logo     = (isset( $general_main_logo ) && !empty( $general_main_logo ) ? wp_get_attachment_image($general_main_logo['attachment_id'], 'full', false, array(
      'class'  => 'img-responsive',
      'alt'    => get_bloginfo( 'name' )
   ) ) : '<img class="img-responsive" width="160" height="60" src="'. MEDIZCO_IMG . '/logo/logo.png' .'" alt="'.get_bloginfo( 'name' ).'">');

?>

<header id="header" class="header header-standard <?php echo esc_attr( $default_class); ?>">
      <div class="header-wrapper">
            <div class="container">
               <nav class="navbar navbar-expand-lg navbar-light">
                        <!-- logo-->
                     <a class="logo" href="<?php echo esc_url(home_url('/')); ?>">
                       <?php echo $site_logo; ?>
                     </a>
                     <button class="navbar-toggler" type="button" data-toggle="collapse"
                           data-target="#primary-nav" aria-controls="primary-nav" aria-expanded="false"
                           aria-label="Toggle navigation">
                           <span class="navbar-toggler-icon"><i class="icon icon-menu"></i></span>
                     </button>
                     
                     <?php get_template_part( 'template-parts/navigations/nav', 'primary' ); ?>
               </nav>
            </div><!-- container end-->
   </div><!-- header wrapper end-->
</header>

