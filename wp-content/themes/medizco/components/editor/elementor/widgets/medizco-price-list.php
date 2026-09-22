<?php

namespace Elementor;

if ( ! defined( 'ABSPATH' ) ) exit;

class Medizco_Price_List_Widget extends Widget_Base {

    public function get_name() {
        return 'medizco-price-list';
    }


    public function get_title() {
        return esc_html__( 'Medizco Price List', 'medizco' );
    }

    public function get_icon() {
        return 'eicon-bullet-list';
    }

    public function get_categories() {
        return ['medizco-elements'];
    }

    protected function register_controls() {

        $this->start_controls_section(
            'medizco_pricelist_contents',
            [
                'label'         => __( 'Contents', 'medizco' ),
                'tab'           => Controls_Manager::TAB_CONTENT,
                'label_block'   => true,
            ]
        );
            $repeater = new \Elementor\Repeater();

            $repeater->add_control(
                'text', [
                    'label'         => __( 'Text:', 'medizco' ),
                    'type'          => \Elementor\Controls_Manager::TEXT,
                    'label_block'   => true,
                ]
            );

            $repeater->add_control(
                'price', [
                    'label'         => __( 'Price:', 'medizco' ),
                    'type'          => \Elementor\Controls_Manager::TEXT,
                    'label_block'   => true,
                ]
            );

            $this->add_control(
                'medizco_pricelist',
                [
                    'label'         => __( 'Price List', 'medizco' ),
                    'type'          => \Elementor\Controls_Manager::REPEATER,
                    'fields'        => $repeater->get_controls(),
                    'title_field'   => '{{{ text }}}',
                ]
            );
        $this->end_controls_section();

        $this->start_controls_section(
            'medizco_pricelist_styles',
            [
                'label'         => __( 'List', 'medizco' ),
                'tab'           => Controls_Manager::TAB_STYLE,
                'label_block'   => true,
            ]
        );
            $this->add_control(
                'medizco_pricelist_color',
                [
                    'label'     => __( 'Color', 'medizco' ),
                    'type'      => Controls_Manager::COLOR,
                    'default'   => '',
                    'selectors' => [
                        '{{WRAPPER}} .medizco_price_list' => 'color: {{VALUE}}'
                    ],
                ]
            );

            $this->add_group_control(
                Group_Control_Typography::get_type(),
                [
                    'name'              => 'medizco_pricelist_font',
                    'label'             => __( 'Typography', 'medizco' ),
                    'selector'          => '{{WRAPPER}} .medizco_price_list',
                ]
            );
        $this->end_controls_section();
    }

    protected function render( ) {
        $settings = $this->get_settings_for_display();

        if ( $settings['medizco_pricelist'] ):
        ?>
            <ul class="medizco_price_list">
                <?php foreach ( $settings['medizco_pricelist'] as $pricelistItem ): ?>
                <li>
                    <span class="text"><?php echo esc_html( $pricelistItem['text'] ); ?></span>
                    <span class="price"><?php echo esc_html( $pricelistItem['price'] ); ?></span>
                </li>
                <?php endforeach; ?>
            </ul>
        <?php
        endif;
    }

    protected function content_template() { }
}