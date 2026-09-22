<?php if (!defined('ABSPATH')) die('Direct access forbidden.');

/**
 * enqueue all theme scripts and styles
 */

// Stylesheets
// ----------------------------------------------------------------------------------------
if ( !is_admin() ):
    // 3rd Party CSS
    wp_enqueue_style( 'medizco-fonts', medizco_google_fonts_url(['Roboto:400,500,700', 'Exo:300,300i,400,700,700i,900']), null,  null );
    wp_enqueue_style( 'bootstrap',  MEDIZCO_CSS . '/bootstrap.min.css', null,  MEDIZCO_VERSION );
    wp_enqueue_style( 'font-awesome',  MEDIZCO_CSS . '/font-awesome.css', null,  MEDIZCO_VERSION );
    wp_enqueue_style( 'slick',  MEDIZCO_CSS . '/slick.css', null,  MEDIZCO_VERSION );

    // theme css
    wp_enqueue_style( 'medizco-blog',  MEDIZCO_CSS . '/blog.css', null,  MEDIZCO_VERSION );
    wp_enqueue_style( 'medizco-gutenberg-custom',  MEDIZCO_CSS . '/gutenberg-custom.css', null,  MEDIZCO_VERSION );
    wp_enqueue_style( 'medizco-master',  MEDIZCO_CSS . '/master.css', null,  MEDIZCO_VERSION );
    wp_enqueue_style( 'medizco-woocommerce',  MEDIZCO_CSS . '/woocommerce.css', null,  MEDIZCO_VERSION );

    if ( is_rtl() ):
      wp_enqueue_style( 'medizco-master-rtl',  MEDIZCO_CSS . '/master-rtl.css', null,  MEDIZCO_VERSION );
    endif;
endif;

// Javascripts
// ----------------------------------------------------------------------------------------
if ( !is_admin() ):
   // 3rd party scripts
   wp_enqueue_script( 'bootstrap',  MEDIZCO_JS . '/bootstrap.min.js', array( 'jquery' ),  MEDIZCO_VERSION, true );

   wp_enqueue_script( 'slick',  MEDIZCO_JS . '/slick.min.js', array( 'jquery' ),  MEDIZCO_VERSION, true );

   // theme js
   wp_enqueue_script( 'medizco-script',  MEDIZCO_JS . '/script.js', array( 'jquery' ),  MEDIZCO_VERSION, true );

    // Load WordPress Comment js
    if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
        wp_enqueue_script( 'comment-reply' );
    }
endif;
