<div class="footer_copyright">
   <div class="container">
      <div class="footer_copyright_text wow fadeInUp" data-wow-duration="1.5s" data-wow-delay="300ms">
         <?php 
            $copyright_text = medizco_option('footer_copyright', '&copy; '.date('Y').' , Medizco. All Rights Reserved.');

            echo medizco_kses( $copyright_text );
         ?>
      </div>
   </div>
</div>

<?php get_template_part( 'template-parts/footer/back-to-top' ); ?>
