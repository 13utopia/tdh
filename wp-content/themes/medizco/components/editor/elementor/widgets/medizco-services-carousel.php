<?php

namespace Elementor;

if ( ! defined( 'ABSPATH' ) ) exit;

class Medizco_Services_Carousel_Widget extends Widget_Base {

    public function get_name() {
        return 'medizco-services-carousel';
    }


    public function get_title() {
        return esc_html__( 'Medizco Services Carousel', 'medizco' );
    }

    public function get_icon() {
        return 'eicon-slider-push';
    }

    public function get_categories() {
        return ['medizco-elements'];
    }

    protected function register_controls() {
        $this->start_controls_section(
            'medizco_servicescarousel_contents',
            [
                'label'         => __( 'Contents', 'medizco' ),
                'tab'           => Controls_Manager::TAB_CONTENT,
                'label_block'   => true,
            ]
        );
            $this->add_control(
                'medizco_servicescarousel_gallery',
                [
                    'label'         => __( 'Images', 'medizco' ),
                    'type'          => \Elementor\Controls_Manager::GALLERY,
                    'label_block'   => true,
                ]
            );
        $this->end_controls_section();

        $this->start_controls_section(
            'medizco_servicescarousel_styles',
            [
                'label'         => __( 'Styles', 'medizco' ),
                'tab'           => Controls_Manager::TAB_STYLE,
                'label_block'   => true,
            ]
        );
            $this->add_control(
                'medizco_servicescarousel_thumbs_ov',
                [
                    'label'     => __( 'Thumbs Overlay', 'medizco' ),
                    'type'      => \Elementor\Controls_Manager::COLOR,
                    'default'   => '',
                    'selectors' => [
                        '{{WRAPPER}} .carousel_thumbs > .swiper-slide:before' => 'background-color: {{VALUE}}',
                    ],
                ]
            );
        $this->end_controls_section();
    }

    protected function render( ) {
        $settings = $this->get_settings_for_display();
        ?>
            <div class="medizco_services_carousels">
                <div class="carousel_main swiper-container">
                    <div class="swiper-wrapper">
                        <?php foreach ( $settings['medizco_servicescarousel_gallery'] as $img ): ?>
                            <a href="<?php echo esc_url( $img['url'] ); ?>" class="swiper-slide">
                                <?php echo wp_get_attachment_image( $img['id'], 'medium_large' ); ?>
                            </a>
                        <?php endforeach; ?>
                    </div>
                </div>

                <div class="carousel_thumbs swiper-container">
                    <div class="swiper-wrapper">
                        <?php foreach ( $settings['medizco_servicescarousel_gallery'] as $img ): ?>
                            <div class="swiper-slide">
                                <?php echo wp_get_attachment_image( $img['id'], 'medium' ); ?>
                            </div>
                        <?php endforeach; ?>
                    </div>
                </div>
            </div>
        <?php
    }

    protected function content_template() {}
}
