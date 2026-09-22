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

    $banner_settings          = medizco_option('blog_banner_setting');


    // Title
    if ( ! empty( $banner_settings['blog_banner_title'] ) ):
        $banner_title = $banner_settings['blog_banner_title'];
    endif;

    // Image
    $bn_img = ( is_array($banner_settings['blog_banner_image']) && !empty($banner_settings['blog_banner_image']['url']) ? wp_get_attachment_image($banner_settings['blog_banner_image']['attachment_id'], 'full', false, array(
        'alt'   => esc_attr($banner_title),
        'class' => 'w-100'
    )) : '<img src="'. MEDIZCO_IMG .'/banner/page-banner-img.jpg'.'" width="1920" height="400" class="w-100" alt="'.get_the_title().'" >');

    // Background Image
    if( is_array( $banner_bgimg ) && ! empty( $banner_bgimg['url'] )):
        $banner_bgimg = $banner_bgimg['url'];
    elseif ( is_array($banner_settings['blog_banner_bg']) && ! empty( $banner_settings['blog_banner_bg']['url'] )):
        $banner_bgimg = $banner_settings['blog_banner_bg']['url'];
    else:
        $banner_bgimg = MEDIZCO_IMG.'/banner/page-banner-bg.png';
    endif;

    // Show
    $show = ( isset( $banner_settings['blog_show_banner'] ) ) ? $banner_settings['blog_show_banner'] : 'yes';

    // Breadcumb
    $show_breadcrumb = ( isset( $banner_settings['blog_show_breadcrumb'] ) ) ? $banner_settings['blog_show_breadcrumb'] : 'yes';

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
    $show                           = 'yes';
    $show_breadcrumb                = 'yes';
    $banner_bottom_bg_overlay_color = "rgba(28, 186, 159, 0.68)";
    $banner_breadcumb_title_color   =  "rgba(28, 186, 159, 1)";
};

if ( ! empty( $banner_bgimg ) ):
    $banner_bgimg = 'background-image: url('.esc_url( $banner_bgimg ).');';
    $banner_bgovl = ' overlay';
endif;


?>

<?php if( isset( $show ) && $show == 'yes' ): ?>
<div class="page_banner">
    <?php if ( $bn_img ): ?>
    <div class="page_banner_img">
        <?php echo $bn_img; ?>
    </div>
    <?php endif; ?>

    <div class="page_banner_content <?php echo esc_attr( $banner_bgovl ); ?>" style="<?php echo esc_attr( $banner_bgimg ); ?>; --banner-overlay-color: <?php echo esc_attr( $banner_bottom_bg_overlay_color ); ?>; --banner-breadcumb-color: <?php echo esc_attr( $banner_breadcumb_title_color ); ?>">
        <div class="container d-lg-flex justify-content-between">
            <h1 class="page_banner_title">
                <?php
                if( !is_single() ):
                    if ( is_archive() ):
                        the_archive_title();
                    elseif ( is_home() ):
                        if('' !=$banner_title) {
                            echo esc_html( $banner_title );
                        }else{
                            echo esc_html__( 'Blog Page', 'medizco' );
                        }
                    else:
                        echo esc_html( $banner_title );
                    endif;
                else:
                    the_title();
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
