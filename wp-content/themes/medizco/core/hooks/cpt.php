<?php if (!defined('ABSPATH')) die('Direct access forbidden.');
/**
 * hooks for wp blog part
 */

// if there is no excerpt, sets a defult placeholder
// ----------------------------------------------------------------------------------------

if ( class_exists( 'MedizcoCustomPost\Medizco_CustomPost' ) ):
    // Doctors
    $doctors = new MedizcoCustomPost\Medizco_CustomPost( 'medizco' );
	$doctors->xs_init('medizco-doctor', 'Doctor', 'Doctors', array(
        'menu_icon'             => 'dashicons-id-alt',
		'supports'	            => array( 'title', 'editor', 'thumbnail', 'page-attributes' ),
		'rewrite'	            => array( 'slug' => 'doctor' ),
		'exclude_from_search'   => true,
    ));
    

    // Doctor Departments
    $doctors_tax = new MedizcoCustomPost\Medizco_Taxonomies( 'medizco' );
    $doctors_tax->xs_init( 'medizco-departments', 'Department', 'Departments', 'medizco-doctor' );

    
    // Services
    $services = new MedizcoCustomPost\Medizco_CustomPost( 'medizco' );
	$services->xs_init('medizco-service', 'Service', 'Services', array(
        'menu_icon'             => 'dashicons-pressthis',
		'supports'	            => array( 'title', 'editor', 'page-attributes' ),
		'rewrite'	            => array( 'slug' => 'service' ),
		'exclude_from_search'   => true,
    ));


    // Preloader
    function medizco_preloader() {
        $preloader = medizco_option( 'show_preloader' );

        if ( isset( $preloader['show_preloader'] ) && 'yes' == $preloader['show_preloader'] ):
            echo '<div class="medizco-preloder">';
            
            if ( 'custom' == $preloader['yes']['preloader_style']['svg_style'] && !empty($preloader['yes']['preloader_style']['custom']['custom_svg'])):
                echo  $preloader['yes']['preloader_style']['custom']['custom_svg'] ;
            else:
                $preloaderImgUrl = MEDIZCO_IMG.'/preloader/'.$preloader['yes']['preloader_style']['simple']['preloader'].'.svg';
                echo  '<img src="'. esc_url( $preloaderImgUrl ) .'" width="50" alt="preloader">';
            endif;

            echo '</div>';
        endif;
    }
    add_action('elementskit/template/before_header', 'medizco_preloader' );


    // Back To Top Button
    function medizco_back_to_top_btn() {
        get_template_part( 'template-parts/footer/back-to-top' );
    }
    add_action('elementskit/template/after_footer', 'medizco_back_to_top_btn' );
endif;
