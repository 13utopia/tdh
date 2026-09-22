<?php

$bn_img                         = '';
$banner_image                   = '';
$banner_bgimg                   = '';
$banner_bgovl                   = '';
$banner_title                   = '';
$banner_style                   = 'full';
$banner_bottom_bg_overlay_color = "";
$banner_breadcumb_title_color   = "";

if ( defined( 'FW' ) ) {

    $banner_settings     = medizco_option('page_banner_setting');
    $banner_meta_image   = medizco_meta_option( get_the_ID(), 'header_image' );
    $banner_global_image = isset($banner_settings['banner_page_image']['url']) ? $banner_settings['banner_page_image']['url'] : '';
    $banner_bgimg        = medizco_meta_option( get_the_ID(), 'header_bg_image' );
    $show_page_banner    = isset($banner_settings['page_show_banner']) ? $banner_settings['page_show_banner'] : 'yes';
    $single_page_img     = isset($banner_meta_image['url']) ? $banner_meta_image['url'] : '';
    $banner_bgimg_page   = isset($banner_bgimg['url']) ? $banner_bgimg['url'] : '';
    $banner_bgimg_global = isset($banner_settings['banner_page_bg']['url']) ? $banner_settings['banner_page_bg']['url'] : '';
    // Title
    if( ! empty( medizco_meta_option( get_the_ID(), 'header_title' ))):
        $banner_title = medizco_meta_option( get_the_ID(), 'header_title' );
    elseif ( ! empty( $banner_settings['banner_page_title'] )):
        $banner_title = $banner_settings['banner_page_title'];
    else:
        $banner_title = get_the_title();
    endif;
    
    // Image
    //from single
    if( $show_page_banner == 'yes' && ! empty( $single_page_img )):
        $bn_img = $single_page_img;
    elseif ($show_page_banner == 'yes' && ! empty( $banner_global_image )):
        $bn_img = $banner_global_image;
    else:
        $bn_img = MEDIZCO_IMG .'/banner/page-banner-img.jpg';
    endif;

    // Background Image
    if( $show_page_banner == 'yes' &&  ! empty( $banner_bgimg_page )):
        $banner_bgimg =  $banner_bgimg_page;
    elseif ( $show_page_banner == 'yes' &&  ! empty( $banner_bgimg_global )):
        $banner_bgimg = $banner_bgimg_global;
    else:
        $banner_bgimg = MEDIZCO_IMG.'/banner/page-banner-bg.png';
    endif;
    
    // Show
    $show = ( isset( $banner_settings['page_show_banner'] ) ) ? $banner_settings['page_show_banner'] : 'yes';

    // Breadcumb
    $show_breadcrumb = ( isset( $banner_settings['page_show_breadcrumb'] ) ) ? $banner_settings['page_show_breadcrumb'] : 'yes';

    // page banner background
    if (isset($banner_settings['banner_bottom_bg_overlay_color']) && $banner_settings['banner_bottom_bg_overlay_color'] !== "") {
        $banner_bottom_bg_overlay_color = $banner_settings['banner_bottom_bg_overlay_color'];
    } else {
        $banner_bottom_bg_overlay_color = "rgba(28, 186, 159, 0.68)";
    }

    // breadcumb title color
    if (isset($banner_settings['banner_breadcumb_title_color']) && $banner_settings['banner_breadcumb_title_color'] !== "") {
        $banner_breadcumb_title_color = $banner_settings['banner_breadcumb_title_color'];
    } else {
        $banner_breadcumb_title_color = "rgba(28, 186, 159, 1)";
    }


} else {
    // Default
    $banner_image                   = '';
    $banner_bgimg                   = '';
    $banner_title                   = get_the_title();
    $show                           = 'yes';
    $show_breadcrumb                = 'yes';
    $banner_bottom_bg_overlay_color = "rgba(28, 186, 159, 0.68)";
    $banner_breadcumb_title_color   =  "rgba(28, 186, 159, 1)";
};


if ( ! empty( $banner_bgimg )):
    $banner_bgimg = 'background-image: url('.esc_url( $banner_bgimg ).');';
    $banner_bgovl = ' overlay';
endif;

?>

<?php if( isset( $show ) && $show == 'yes' ): ?>
<div class="page_banner">
    <?php if ( $bn_img ): ?>
    <div class="page_banner_img">
       <img src="<?php echo esc_url($bn_img) ?>" alt="<?php
                if ( is_archive() ):
                    the_archive_title();
                else:
                    echo esc_html( $banner_title );
                endif;
                ?>">
    </div>
    <?php endif; ?>

    <div class="page_banner_content <?php echo esc_attr( $banner_bgovl ); ?>" style="<?php echo esc_attr( $banner_bgimg ); ?>; --banner-overlay-color: <?php echo esc_attr( $banner_bottom_bg_overlay_color ); ?>; --banner-breadcumb-color: <?php echo esc_attr( $banner_breadcumb_title_color ); ?>">
        <div class="container d-lg-flex justify-content-between">
            <h1 class="page_banner_title">
                <?php
                if ( is_archive() ):
                    the_archive_title();
                else:
                    echo esc_html( $banner_title );
                endif;
                ?>
            </h1>

            <?php
            if( isset( $show_breadcrumb ) && 'yes' == $show_breadcrumb ):
                medizco_get_breadcrumbs('-');
            endif;
            ?>
        </div>
    </div>
</div><!-- .medizco_banner -->
<?php
endif;
