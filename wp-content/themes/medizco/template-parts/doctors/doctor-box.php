<?php
$doctor_role = medizco_meta_option( get_the_ID(), 'doctor_role' );
$doctor_icon = medizco_meta_option( get_the_ID(), 'doctor_icon' );
$doctor_sc_icons = medizco_meta_option( get_the_ID(), 'doctor_social' );
?>

<div class="doctor_box">
    <div class="doctor_box_img">
        <?php the_post_thumbnail( 'medium_large' ); ?>
        <?php if (!empty($doctor_sc_icons)) { ?>
        <ul class="doctor_box_social d-flex flex-column justify-content-end">
            <?php foreach ( $doctor_sc_icons as $doctor_sc_icon ): ?>
            <li>
                <a href="<?php echo esc_url( $doctor_sc_icon['link'] ); ?>" target="_blank">
                    <i class="<?php echo esc_attr( $doctor_sc_icon['icon'] ); ?>" style="color: <?php echo esc_attr( $doctor_sc_icon['color'] ); ?>;"></i>
                    <span style="background-color: <?php echo esc_attr( $doctor_sc_icon['color'] ); ?>;">
                        <?php echo esc_html( $doctor_sc_icon['title'] ); ?>
                    </span>
                </a>
            </li>
            <?php endforeach; ?>
        </ul>
        <?php } ?>
    </div>

    <!-- <?php if ( !empty($doctor_icon) && $doctor_icon['type'] !== 'none' && $doctor_icon['type'] === 'icon-font' ) { ?>
    <div class="doctor_box_icon">
        <i class="<?php echo esc_attr( $doctor_icon['icon-class'] ); ?> doctor_box_icon_item"></i>
    </div>
    <?php } ?>
    <?php var_dump($doctor_icon); ?>
    <?php if ( !empty($doctor_icon) && $doctor_icon['type'] !== 'none' && $doctor_icon['type'] === 'custom-upload' ) { ?>
    <div class="doctor_box_icon">
        <?php echo wp_get_attachment_image( $doctor_icon["attachment-id"], "", "", array( "class" => "doctor_box_icon_item" ) ); ?>
    </div>
    <?php } ?> -->

    <?php if ( !empty($doctor_icon) && $doctor_icon['type'] !== 'none' && $doctor_icon['type'] === 'icon-font' ) { ?>
    <div class="doctor_box_icon">
        <i class="<?php echo esc_attr( $doctor_icon['icon-class'] ); ?> doctor_box_icon_item"></i>

    </div>
    <?php } ?>
    <?php if ( !empty($doctor_icon) && $doctor_icon['type'] !== 'none' && $doctor_icon['type'] === 'custom-upload' ) { ?>
    <div class="doctor_box_icon">
        <?php echo wp_get_attachment_image( $doctor_icon["attachment-id"], "", "", array( "class" => "doctor_box_icon_item" ) ); ?>
    </div>
    <?php } ?>


    <div class="doctor_box_content">
        <h3 class="doctor_box_title"><?php the_title(); ?></h3>

        <?php if ( $doctor_role ): ?>
        <p class="doctor_box_role"><?php echo esc_html( $doctor_role ); ?></p>
        <?php endif; ?>
    </div>

    <a href="<?php the_permalink(); ?>" class="doctor_box_link"></a>
</div>
