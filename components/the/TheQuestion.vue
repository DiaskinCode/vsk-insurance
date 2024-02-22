<template>
  <div
    id="question"
    class="question container-wrapper bg-g"
  >
    <div class="container fd-c ai-c py-100 py-50-mb">
      <h2 class="header-text mb-50 mb-25-mb">
        Ответы на вопросы
      </h2>
      <div class="row w-100 gy-0 gy-5-mb gx-25">
        <div class="col-6 col-12-mb">
          <div class="w-100">
            <AppAccordion
              class="w-100 row gy-25 gx-0 gy-5-mb"
              multiple
              :active-index="activeLeft"
            >
              <AccordionTab
                class="col-12"
                header="Зачем мне страховаться от несчастного случая?"
                :disabled="disabled"
              >
                При наступлении страхового случая страховая компания произведет денежную
                выплату, чтобы обеспечить финансовую поддержку вам и вашей семье
              </AccordionTab>
              <AccordionTab
                class="col-12"
                header="Куда обращаться в случае страхового события?"
                :disabled="disabled"
              >
                <ul>
                  <li>
                    заполнить Заявление и заявить о событии дистанционно на сайте
                    Компании/мобильном приложении "ВСК Страхование"
                  </li>
                  <li>
                    или заполнить Заявление в офисе урегулирования САО «ВСК» региона
                  </li>
                </ul>
              </AccordionTab>
              <AccordionTab
                class="col-12"
                header="Какая территория покрытия по моему полису?"
                :disabled="disabled"
              >
                Полис действует по всему миру,
                за исключением зон вооруженных конфликтов, зон ведения военных, боевых действий
                (операций) или иных подобных мероприятий, зон проведения специальных операций,
                включая антитеррористические операций и иных подобных мероприятий, территорий
                на которых введено чрезвычайное либо военное положение, территорий гражданских
                войн, народных волнений всякого рода или забастовок, включая революции.
              </AccordionTab>
            </AppAccordion>
          </div>
        </div>
        <div class="col-6 col-12-mb">
          <div class="w-100">
            <AppAccordion
              class="w-100 row gy-25 gx-0 gy-5-mb"
              multiple
              :active-index="activeRight"
            >
              <AccordionTab
                class="col-12"
                header="Какие документы я получу после оплаты полиса?"
                :disabled="disabled"
              >
                Сразу после оплаты Вы получите на e-mail: полис страхования, правила
                страхования и чек об оплате.
              </AccordionTab>
              <AccordionTab
                class="col-12"
                header="Что делать в случае страхового события?"
                :disabled="disabled"
              >
                <p class="mb-5">
                  1. Застрахованному необходимо в течение 24 часов с момента несчастного
                  случая обратиться в медицинское учреждение для объективной оценки вреда,
                  причиненного здоровью, и получить медицинские документы, удостоверяющие
                  факт случая.
                </p>
                <p class="mb-5">
                  2. Страхователь/застрахованный обязан в течение 30 дней со дня причинения
                  вреда здоровью Застрахованного уведомить о событии Страховщика любым доступным
                  образом (для уведомления о событии документы не требуются).
                </p>
                <p>
                  Для рассмотрения Страховщиком произошедшего события необходимо подать
                  Страховщику Заявление и предоставить всю необходимую информацию и
                  подтверждающие документы (перечень документов по каждому виду события
                  обозначены в Правилах страхования)
                </p>
              </AccordionTab>
            </AppAccordion>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TheQuestion',
  props: {},
  data: () => ({
    activeLeftDesk: [0, 1, 2],
    activeRightDesk: [0, 1],
    activeLeftMobile: [],
    activeRightMobile: [],
  }),
  computed: {
    activeLeft() {
      return this.$mq === 'mb' ? this.activeLeftMobile : this.activeLeftDesk;
    },
    activeRight() {
      return this.$mq === 'mb' ? this.activeRightMobile : this.activeRightDesk;
    },
    disabled() {
      return this.$mq !== 'mb';
    },
  },
  methods: {},
}
</script>

<style lang="scss">
.question {
  li {
    position: relative;
    padding-left: 1.5rem;
  }
  li::before {
    position: absolute;
    left: 0;
    font-size: 3rem;
    top: -0.7rem;
    content: '.';
  }
}
</style>
