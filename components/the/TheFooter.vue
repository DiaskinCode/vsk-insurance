<template>
  <footer class="footer container fd-c py-50 c-t15">
    <div class="d-f jc-sb">
      <div>
        <AppLogo
          src="\logo-bw.png"
        />
        <div class="fs-16 lh-140">
          © Страховое акционерное общество “ВСК”, 2002–2022
        </div>
        <AppLinkInner
          class="fs-16 lh-140"
          href="\"
          text="Политика в отношении обработки персональных данных"
        />
      </div>
      <div class="d-f fd-c fs-16 lh-140">
        <a
          v-for="(link, i) in links"
          :key="i"
          class="c-t15"
          :class="{'mt-10': i !== 0}"
          :href="link.href"
        >{{link.label}}</a>
      </div>
      <div>
        <a
          class="fw-6 fs-25 lh-140 c-t15"
          href="tel:8-800-775-15-75"
        >
          8 (800) 775-15-75
        </a>
        <div class="fs-20 mt-5">
          г. Москва, ул. Островная, 4
        </div>
        <div class="d-f mt-20">
          <a
            v-for="(link, i) in linksSocial"
            :key="i"
            :class="{'ml-10': i !== 0, [link.class]: true}"
            :href="link.href"
          >
            <img
              :src="link.icon"
              alt="social-link"
            >
          </a>
        </div>
      </div>
    </div>
    <div class="d-f mt-50">
      <div>
        <img
          class="footer__icon mr-15"
          src="/warning.svg"
          alt="warning"
        >
      </div>
      <div class="fs-12 lh-130 footer__text">
        ИНФОРМАЦИЮ, ПОДЛЕЖАЩУЮ РАСКРЫТИЮ В СООТВЕТСТВИИ С ТРЕБОВАНИЯМИ ФЕДЕРАЛЬНОГО ЗАКОНА
        «О РЫНКЕ ЦЕННЫХ БУМАГ» (ОТ 22.04.1996 N 39-ФЗ) И ПОЛОЖЕНИЯ О РАСКРЫТИИ ИНФОРМАЦИИ
        ЭМИТЕНТАМИ ЭМИССИОННЫХ ЦЕННЫХ БУМАГ (УТВ. БАНКОМ РОССИИ 30.12.2014 N 454-П),
        САО «ВСК» РАСКРЫВАЕТ НА СТРАНИЦЕ В СЕТИ ИНТЕРНЕТ ООО «ИНТЕРФАКС-ЦРКИ» – ИНФОРМАЦИОННОГО
        АГЕНТСТВА, АККРЕДИТОВАННОГО ЦБ РФ НА РАСКРЫТИЕ ИНФОРМАЦИИ, ПО АДРЕСУ:
        <AppLinkInner
          text="HTTP://WWW.E-DISCLOSURE.RU/PORTAL/COMPANY.ASPX?ID=1968"
          href="HTTP://WWW.E-DISCLOSURE.RU/PORTAL/COMPANY.ASPX?ID=1968"
        />
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'TheFooter',
  props: {},
  data: () => ({
    links: [
      {
        href: '#include',
        label: 'Что включает полис',
      },
      {
        href: '#benefit',
        label: 'Преимущества',
      },
      {
        href: '#calculate',
        label: 'Калькулятор',
      },
      {
        href: '#question',
        label: 'FAQ',
      },
    ],
    linksSocial: [
      {
        href: '#include',
        icon: '/link-icons/yt.svg',
        class: 'footer__link-social--yt',
      },
      {
        href: '#benefit',
        icon: '/link-icons/vk.svg',
        class: 'footer__link-social--vk',
      },
      {
        href: '#calculate',
        icon: '/link-icons/ok.svg',
        class: 'footer__link-social--ok',
      },
    ]
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
.footer {
  /* .footer__link-social */
  &__link-social {
    /* .footer__link-social--yt */
    &--yt {
      width: 2.913rem;
      height: 2.066rem;
    }
    /* .footer__link-social--vk */
    &--vk {
      width: 3.7rem;
      height: 2.1rem;
    }
    /* .footer__link-social--ok */
    &--ok {
      width: 2.733rem;
      height: 2.733rem;
    }
  }
  /* .footer__icon */
  &__icon {
    width: 5.9rem;
    height: 5.9rem;
  }
  /* .footer__text */
  &__text {
    letter-spacing: .04rem;
  }
}
</style>
