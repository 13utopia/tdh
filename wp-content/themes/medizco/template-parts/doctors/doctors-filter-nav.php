<?php
$doc_deprts = get_terms( 'medizco-departments' );

if ( !empty( $doc_deprts ) ):
?>
    <ul class="filter_nav d-flex flex-wrap justify-content-center">
        <?php
        $i = 0;
        foreach( $doc_deprts as $doc_deprt ):
            $isActive = $i == 0 ? 'active' : '';
            ?>
            <li class="filter <?php echo esc_attr( $isActive ); ?>" data-filter=".<?php echo esc_attr( $doc_deprt->slug, 'medizco' ); ?>"><?php echo esc_html( $doc_deprt->name ); ?></li>
            <?php
        $i++;
        endforeach;
        ?>
    </ul>
<?php
endif;
