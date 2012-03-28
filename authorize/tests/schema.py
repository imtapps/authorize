SCHEMA = """\
<?xml version="1.0" encoding="utf-8"?>
<xs:schema targetNamespace="AnetApi/xml/v1/schema/AnetApiSchema.xsd" elementFormDefault="qualified" xmlns:anet="AnetApi/xml/v1/schema/AnetApiSchema.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<!-- 
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	 Request type definitions begin here
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	-->
	<xs:simpleType name="numericString">
		<xs:restriction base="xs:string">
			<xs:pattern value="[0-9]+" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:complexType name="ArrayOfLong">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="long" nillable="false" type="xs:long" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ArrayOfNumericString">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="numericString" nillable="false" type="anet:numericString" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ArrayOfString">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="string" nillable="false" type="xs:string" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ArrayOfLineItem">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="lineItem" nillable="false" type="anet:lineItemType" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ArrayOfBatchStatisticType">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="statistic" type="anet:batchStatisticType" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ArrayOfBatchDetailsType">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="batch" type="anet:batchDetailsType" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ArrayOfTransactionSummaryType">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="transaction" type="anet:transactionSummaryType" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ArrayOfSetting">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="setting" nillable="false" type="anet:settingType" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ArrayOfFDSFilter">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="FDSFilter" nillable="false" type="anet:FDSFilterType" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ArrayOfPermissionType">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="permission" nillable="false" type="anet:permissionType" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:simpleType name="bankAccountTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="checking" />
			<xs:enumeration value="savings" />
			<xs:enumeration value="businessChecking" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="echeckTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="PPD" />
			<xs:enumeration value="WEB" />
			<xs:enumeration value="CCD" />
			<xs:enumeration value="TEL" />
			<xs:enumeration value="ARC" />
			<xs:enumeration value="BOC" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="paymentMethodEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="creditCard" />
			<xs:enumeration value="eCheck" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="cardTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="Visa" />
			<xs:enumeration value="MasterCard" />
			<xs:enumeration value="AmericanExpress" />
			<xs:enumeration value="Discover" />
			<xs:enumeration value="JCB" />
			<xs:enumeration value="DinersClub" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="accountTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="Visa" />
			<xs:enumeration value="MasterCard" />
			<xs:enumeration value="AmericanExpress" />
			<xs:enumeration value="Discover" />
			<xs:enumeration value="JCB" />
			<xs:enumeration value="DinersClub" />
			<xs:enumeration value="eCheck" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="customerTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="individual" />
			<xs:enumeration value="business" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="ARBSubscriptionUnitEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="days" />
			<xs:enumeration value="months" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="validationModeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="none" />
			<xs:enumeration value="testMode" /> <!-- Free test-mode transaction. No validation against live cardholder account. -->
			<xs:enumeration value="liveMode" /> <!-- Validate against live cardholder account for 0.00 if available, 0.01 otherwise. -->
			<xs:enumeration value="oldLiveMode" /> <!-- Validate against live cardholder account for 0.01 even if 0.00 option is available. NOT RECOMMENDED. Use of this option can result in fines from your processor. -->
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="splitTenderStatusEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="completed" />
			<xs:enumeration value="held" />
			<xs:enumeration value="voided" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="ARBSubscriptionStatusEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="active" />
			<xs:enumeration value="expired" />
			<xs:enumeration value="suspended" />
			<xs:enumeration value="canceled" />
			<xs:enumeration value="terminated" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="transactionTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="authOnlyTransaction" />
			<xs:enumeration value="authCaptureTransaction" />
			<xs:enumeration value="captureOnlyTransaction" />
			<xs:enumeration value="refundTransaction" />
			<xs:enumeration value="priorAuthCaptureTransaction" />
			<xs:enumeration value="voidTransaction" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="transactionStatusEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="authorizedPendingCapture" />
			<xs:enumeration value="capturedPendingSettlement" />
			<xs:enumeration value="communicationError" />
			<xs:enumeration value="refundSettledSuccessfully" />
			<xs:enumeration value="refundPendingSettlement" />
			<xs:enumeration value="approvedReview" />
			<xs:enumeration value="declined" />
			<xs:enumeration value="couldNotVoid" />
			<xs:enumeration value="expired" />
			<xs:enumeration value="generalError" />
			<xs:enumeration value="pendingFinalSettlement" />
			<xs:enumeration value="pendingSettlement" />
			<xs:enumeration value="failedReview" />
			<xs:enumeration value="settledSuccessfully" />
			<xs:enumeration value="settlementError" />
			<xs:enumeration value="underReview" />
			<xs:enumeration value="updatingSettlement" />
			<xs:enumeration value="voided" />
			<xs:enumeration value="FDSPendingReview" />
			<xs:enumeration value="FDSAuthorizedPendingReview" />
			<xs:enumeration value="returnedItem" />
			<xs:enumeration value="chargeback" />
			<xs:enumeration value="chargebackReversal" />
			<xs:enumeration value="authorizedPendingRelease" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="settlementStateEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="settledSuccessfully" />
			<xs:enumeration value="settlementError" />
			<xs:enumeration value="pendingSettlement" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="FDSFilterActionEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="reject" />
			<xs:enumeration value="decline" />
			<xs:enumeration value="hold" />
			<xs:enumeration value="authAndHold" />
			<xs:enumeration value="report" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="permissionsEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="API_Merchant_BasicReporting" />
			<xs:enumeration value="Submit_Charge" />
			<xs:enumeration value="Submit_Refund" />
			<xs:enumeration value="Submit_Update" />
			<xs:enumeration value="Mobile_Admin" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:complexType name="driversLicenseType">
		<xs:sequence>
			<!-- Format of number should be string or four X's followed by the last four digits. -->
			<xs:element name="number">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="5" />
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="state">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="2" />
						<xs:maxLength value="2" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- Format of dateOfBirth should be xs:date (1965-01-28) or XX/XX/1965. -->
			<xs:element name="dateOfBirth">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="8" />
						<xs:maxLength value="10" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="driversLicenseMaskedType">
		<xs:sequence>
			<xs:element name="number">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:length value="8" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="state">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="2" />
						<xs:maxLength value="2" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="dateOfBirth">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="8" />
						<xs:maxLength value="10" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="nameAndAddressType">
		<xs:sequence>
			<xs:element name="firstName" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="lastName" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="company" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="address" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="60" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="city" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="40" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="state" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="40" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="zip" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="country" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="60" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="merchantContactType">
		<xs:sequence>
			<xs:element name="merchantName" type="xs:string" minOccurs="0" />
			<xs:element name="merchantAddress" type="xs:string" minOccurs="0" />
			<xs:element name="merchantCity" type="xs:string" minOccurs="0" />
			<xs:element name="merchantState" type="xs:string" minOccurs="0" />
			<xs:element name="merchantZip" type="xs:string" minOccurs="0" />
			<xs:element name="merchantPhone" type="xs:string" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="transRetailInfoType">
		<xs:sequence>
			<xs:element name="marketType" minOccurs="0" type="xs:string" default="2" />
			<xs:element name="deviceType" minOccurs="0" type="xs:string" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="creditCardSimpleType">
		<xs:sequence>
			<!-- Format of cardNumber should be numeric string or four X's followed by the last four digits. -->
			<xs:element name="cardNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="4" />
						<xs:maxLength value="16" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- Format of expirationDate should be gYearMonth (such as 2001-10) or four X's. -->
			<xs:element name="expirationDate">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="4" />
						<xs:maxLength value="7" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="creditCardTrackType">
		<xs:choice>
			<xs:element name="track1" type="xs:string" />
			<xs:element name="track2" type="xs:string" />
		</xs:choice>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="creditCardType">
		<xs:complexContent>
			<xs:extension base="anet:creditCardSimpleType">
				<xs:sequence>
					<!-- cardCode may be passed in for validation but it will not be stored. -->
					<xs:element name="cardCode" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="anet:numericString">
								<xs:minLength value="3" />
								<xs:maxLength value="4" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="creditCardMaskedType">
		<xs:sequence>
			<xs:element name="cardNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:length value="8" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="expirationDate">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="4" />
						<xs:maxLength value="7" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="cardType" type="xs:string" minOccurs="0" /> <!-- anet:cardTypeEnum -->
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ccAuthenticationType">
		<xs:sequence>
			<xs:element name="authenticationIndicator" type="xs:string" />
			<xs:element name="cardholderAuthenticationValue" type="xs:string" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="bankAccountType">
		<xs:sequence>
			<xs:element name="accountType" type="anet:bankAccountTypeEnum" minOccurs="0" />
			<!-- Format of routingNumber should be nine digits or four X's followed by the last four digits. -->
			<xs:element name="routingNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="9" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- Format of accountNumber should be numeric string or four X's followed by the last four digits. -->
			<xs:element name="accountNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="17" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="nameOnAccount">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="22" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="echeckType" type="anet:echeckTypeEnum" minOccurs="0" />
			<xs:element name="bankName" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="checkNumber" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="15" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="bankAccountMaskedType">
		<xs:sequence>
			<xs:element name="accountType" type="anet:bankAccountTypeEnum" minOccurs="0" />
			<xs:element name="routingNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:length value="8" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="accountNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:length value="8" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="nameOnAccount">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="22" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="echeckType" type="anet:echeckTypeEnum" minOccurs="0" />
			<xs:element name="bankName" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="paymentSimpleType">
		<xs:sequence>
			<xs:choice>
				<xs:element name="creditCard" type="anet:creditCardSimpleType" />
				<xs:element name="bankAccount" type="anet:bankAccountType" />
			</xs:choice>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="paymentType">
		<xs:sequence>
			<xs:choice>
				<xs:element name="creditCard" type="anet:creditCardType" />
				<xs:element name="bankAccount" type="anet:bankAccountType" />
				<xs:element name="trackData" type="anet:creditCardTrackType" />
			</xs:choice>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="paymentMaskedType">
		<xs:sequence>
			<xs:choice>
				<xs:element name="creditCard" type="anet:creditCardMaskedType" />
				<xs:element name="bankAccount" type="anet:bankAccountMaskedType" />
			</xs:choice>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="orderType">
		<xs:sequence>
			<xs:element name="invoiceNumber" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="description" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="orderExType">
		<xs:complexContent>
			<xs:extension base="anet:orderType">
				<xs:sequence>
					<xs:element name="purchaseOrderNumber" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:maxLength value="25" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerType">
		<xs:sequence>
			<xs:element name="type" type="anet:customerTypeEnum" minOccurs="0" />
			<xs:element name="id" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="email" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="phoneNumber" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="25" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="faxNumber" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="25" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="driversLicense" type="anet:driversLicenseType" minOccurs="0" />
			<xs:element name="taxId" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="anet:numericString">
						<xs:minLength value="9" />
						<xs:maxLength value="9" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerDataType">
		<xs:sequence>
			<xs:element name="type" type="anet:customerTypeEnum" minOccurs="0" />
			<xs:element name="id" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="email" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="driversLicense" type="anet:driversLicenseType" minOccurs="0" />
			<xs:element name="taxId" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="8" />
						<xs:maxLength value="9" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="merchantAuthenticationType">
		<xs:sequence>
			<xs:element name="name" minOccurs="0" maxOccurs="1">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="25" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:choice maxOccurs="1" minOccurs="1">
				<xs:element name="transactionKey">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:maxLength value="16" />
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
				<xs:element name="sessionToken">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:maxLength value="50" />
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
				<xs:element name="password">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:maxLength value="40" />
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
			</xs:choice>
			<xs:element name="mobileDeviceId" minOccurs="0" maxOccurs="1">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="60" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="paymentScheduleType">
		<xs:sequence>
			<!-- required for a new schedule, optional when updating -->
			<xs:element name="interval" minOccurs="0">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="length">
							<xs:simpleType>
								<xs:restriction base="xs:short">
									<xs:minInclusive value="1" />
									<xs:maxInclusive value="32000" />
								</xs:restriction>
							</xs:simpleType>
						</xs:element>
						<xs:element name="unit" type="anet:ARBSubscriptionUnitEnum" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<!-- required for a new schedule, not allowed when editting existing subscription -->
			<xs:element name="startDate" type="xs:date" minOccurs="0" />
			<!-- required for a new schedule, optional when updating -->
			<xs:element name="totalOccurrences" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:short">
						<xs:minInclusive value="1" />
						<xs:maxInclusive value="32000" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- trialOccurrences is always optional -->
			<xs:element name="trialOccurrences" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:short">
						<xs:minInclusive value="0" />
						<xs:maxInclusive value="32000" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ARBSubscriptionType">
		<xs:sequence>
			<xs:element name="name" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- paymentSchedule is required for a new subscription, optional if updating existing subscription -->
			<xs:element name="paymentSchedule" type="anet:paymentScheduleType" minOccurs="0" />
			<xs:element name="amount" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.01" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="trialAmount" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:fractionDigits value="4" />
						<xs:minInclusive value="0.00" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- required for Create, optional on Update -->
			<xs:element name="payment" type="anet:paymentType" minOccurs="0" />
			<xs:element name="order" type="anet:orderType" minOccurs="0" />
			<xs:element name="customer" type="anet:customerType" minOccurs="0" />
			<xs:element name="billTo" type="anet:nameAndAddressType" minOccurs="0" />
			<xs:element name="shipTo" type="anet:nameAndAddressType" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="mobileDeviceType">
		<xs:sequence>
			<xs:element name="mobileDeviceId" minOccurs="1" maxOccurs="1">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="60" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="description" minOccurs="0" maxOccurs="1">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="60" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="phoneNumber" minOccurs="0" maxOccurs="1">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!--
	===================================================================
	transactionRequestType
	These are the fields that are used for a transaction request.
	===================================================================
	-->
	<xs:complexType name="transactionRequestType">
		<xs:sequence>
			<xs:element name="transactionType" type="xs:string" />
			<xs:element name="amount" type="xs:decimal" minOccurs="0" />
			<xs:element name="payment" type="anet:paymentType" minOccurs="0" />
			<xs:element name="authCode" type="xs:string" minOccurs="0" />
			<xs:element name="refTransId" type="xs:string" minOccurs="0" />
			<xs:element name="splitTenderId" minOccurs="0" type="xs:string" />
			<xs:element name="order" type="anet:orderType" minOccurs="0" />
			<xs:element name="lineItems" type="anet:ArrayOfLineItem" minOccurs="0" />
			<xs:element name="tax" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="duty" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="shipping" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="taxExempt" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:boolean" />
				</xs:simpleType>
			</xs:element>
			<xs:element name="poNumber" type="xs:string" minOccurs="0" />
			<xs:element name="customer" type="anet:customerDataType" minOccurs="0" />
			<xs:element name="billTo" type="anet:customerAddressType" minOccurs="0" />
			<xs:element name="shipTo" type="anet:nameAndAddressType" minOccurs="0" />
			<xs:element name="customerIP" type="xs:string" minOccurs="0" />
			<xs:element name="cardholderAuthentication" type="anet:ccAuthenticationType" minOccurs="0" />
			<xs:element name="retail" type="anet:transRetailInfoType" minOccurs="0" />
			<xs:element name="transactionSettings" type="anet:ArrayOfSetting" minOccurs="0">
				<xs:annotation>
					<xs:documentation>Allowed values for settingName are: emailCustomer, merchantEmail, allowPartialAuth, headerEmailReceipt, footerEmailReceipt, recurringBilling, duplicateWindow, testRequest.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="userFields" minOccurs="0">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="userField" type="anet:userField" minOccurs="0" maxOccurs="20" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="settingType">
		<xs:sequence>
			<xs:element name="settingName" type="xs:string" minOccurs="0" />
			<xs:element name="settingValue" type="xs:string" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="permissionType">
		<xs:sequence>
			<xs:element name="permissionName" type="xs:string" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:simpleType name="settingNameEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="emailCustomer">
				<xs:annotation>
					<xs:documentation>true/false. Used by createTransaction method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="merchantEmail">
				<xs:annotation>
					<xs:documentation>string. Used by createTransaction method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="allowPartialAuth">
				<xs:annotation>
					<xs:documentation>true/false. Used by createTransaction method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="headerEmailReceipt">
				<xs:annotation>
					<xs:documentation>string. Used by createTransaction method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="footerEmailReceipt">
				<xs:annotation>
					<xs:documentation>string. Used by createTransaction method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="recurringBilling">
				<xs:annotation>
					<xs:documentation>true/false. Used by createTransaction method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="duplicateWindow">
				<xs:annotation>
					<xs:documentation>number. Used by createTransaction method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="testRequest">
				<xs:annotation>
					<xs:documentation>true/false. Used by createTransaction method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="hostedProfileReturnUrl">
				<xs:annotation>
					<xs:documentation>string. Used by getHostedProfilePage method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="hostedProfileReturnUrlText">
				<xs:annotation>
					<xs:documentation>string. Used by getHostedProfilePage method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="hostedProfilePageBorderVisible">
				<xs:annotation>
					<xs:documentation>true/false. Used by getHostedProfilePage method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="hostedProfileIFrameCommunicatorUrl">
				<xs:annotation>
					<xs:documentation>string. Used by getHostedProfilePage method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
			<xs:enumeration value="hostedProfileHeadingBgColor">
				<xs:annotation>
					<xs:documentation>#e0e0e0. Used by getHostedProfilePage method.</xs:documentation>
				</xs:annotation>
			</xs:enumeration>
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:complexType name="userField">
		<xs:sequence>
			<xs:element name="name" type="xs:string" minOccurs="0" />
			<xs:element name="value" type="xs:string" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerPaymentProfileBaseType">
		<xs:sequence>
			<xs:element name="customerType" type="anet:customerTypeEnum" minOccurs="0" />
			<xs:element name="billTo" type="anet:customerAddressType" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerPaymentProfileType">
		<xs:complexContent>
			<xs:extension base="anet:customerPaymentProfileBaseType">
				<xs:sequence>
					<xs:element name="payment" type="anet:paymentType" minOccurs="0" />
					<xs:element name="driversLicense" type="anet:driversLicenseType" minOccurs="0" />
					<!-- Format of taxId should be numeric string or four X's followed by the last four digits. -->
					<xs:element name="taxId" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:minLength value="8" />
								<xs:maxLength value="9" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerPaymentProfileExType">
		<xs:complexContent>
			<xs:extension base="anet:customerPaymentProfileType">
				<xs:sequence>
					<xs:element name="customerPaymentProfileId" type="anet:numericString" minOccurs="0" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerPaymentProfileMaskedType">
		<xs:complexContent>
			<xs:extension base="anet:customerPaymentProfileBaseType">
				<xs:sequence>
					<xs:element name="customerPaymentProfileId" type="anet:numericString" minOccurs="0" />
					<xs:element name="payment" type="anet:paymentMaskedType" minOccurs="0" />
					<xs:element name="driversLicense" type="anet:driversLicenseMaskedType" minOccurs="0" />
					<xs:element name="taxId" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:length value="8" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerProfileBaseType">
		<xs:sequence>
			<xs:element name="merchantCustomerId" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="description" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="email" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerProfileType">
		<xs:complexContent>
			<xs:extension base="anet:customerProfileBaseType">
				<xs:sequence>
					<xs:element name="paymentProfiles" type="anet:customerPaymentProfileType" minOccurs="0" maxOccurs="unbounded" />
					<xs:element name="shipToList" type="anet:customerAddressType" minOccurs="0" maxOccurs="unbounded" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerProfileExType">
		<xs:complexContent>
			<xs:extension base="anet:customerProfileBaseType">
				<xs:sequence>
					<xs:element name="customerProfileId" type="anet:numericString" minOccurs="0" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerProfileMaskedType">
		<xs:complexContent>
			<xs:extension base="anet:customerProfileExType">
				<xs:sequence>
					<xs:element name="paymentProfiles" type="anet:customerPaymentProfileMaskedType" minOccurs="0" maxOccurs="unbounded" />
					<xs:element name="shipToList" type="anet:customerAddressExType" minOccurs="0" maxOccurs="unbounded" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerAddressType">
		<xs:complexContent>
			<xs:extension base="anet:nameAndAddressType">
				<xs:sequence>
					<xs:element name="phoneNumber" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:maxLength value="255" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<xs:element name="faxNumber" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:maxLength value="255" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerAddressExType">
		<xs:complexContent>
			<xs:extension base="anet:customerAddressType">
				<xs:sequence>
					<xs:element name="customerAddressId" type="anet:numericString" minOccurs="0" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="extendedAmountType">
		<xs:sequence>
			<xs:element name="amount">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.00" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="name" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="31" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="description" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="lineItemType">
		<xs:sequence>
			<xs:element name="itemId">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="1" />
						<xs:maxLength value="31" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="name">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="1" />
						<xs:maxLength value="31" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="description" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="quantity">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.00" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="unitPrice">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.00" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="taxable" type="xs:boolean" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransAmountType">
		<xs:sequence>
			<xs:element name="amount">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.01" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="tax" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="shipping" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="duty" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="lineItems" type="anet:lineItemType" minOccurs="0" maxOccurs="30" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransOrderType">
		<xs:complexContent>
			<xs:extension base="anet:profileTransAmountType">
				<xs:sequence>
					<xs:element name="customerProfileId" type="anet:numericString" />
					<xs:element name="customerPaymentProfileId" type="anet:numericString" />
					<xs:element name="customerShippingAddressId" type="anet:numericString" minOccurs="0" />
					<xs:element name="order" type="anet:orderExType" minOccurs="0" />
					<xs:element name="taxExempt" type="xs:boolean" minOccurs="0" />
					<xs:element name="recurringBilling" type="xs:boolean" minOccurs="0" />
					<xs:element name="cardCode" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="anet:numericString">
								<xs:minLength value="3" />
								<xs:maxLength value="4" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<xs:element name="splitTenderId" type="anet:numericString" minOccurs="0" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransAuthCaptureType">
		<xs:complexContent>
			<xs:extension base="anet:profileTransOrderType">
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransAuthOnlyType">
		<xs:complexContent>
			<xs:extension base="anet:profileTransOrderType">
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransPriorAuthCaptureType">
		<xs:complexContent>
			<xs:extension base="anet:profileTransAmountType">
				<xs:sequence>
					<xs:element name="customerProfileId" type="anet:numericString" minOccurs="0" />
					<xs:element name="customerPaymentProfileId" type="anet:numericString" minOccurs="0" />
					<xs:element name="customerShippingAddressId" type="anet:numericString" minOccurs="0" />
					<xs:element name="transId" type="anet:numericString" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransCaptureOnlyType">
		<xs:complexContent>
			<xs:extension base="anet:profileTransOrderType">
				<xs:sequence>
					<xs:element name="approvalCode">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:maxLength value="6" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransRefundType">
		<xs:complexContent>
			<xs:extension base="anet:profileTransAmountType">
				<xs:sequence>
					<xs:element name="customerProfileId" type="anet:numericString" minOccurs="0" />
					<xs:element name="customerPaymentProfileId" type="anet:numericString" minOccurs="0" />
					<xs:element name="customerShippingAddressId" type="anet:numericString" minOccurs="0" />
					<!-- Format of creditCardNumberMasked should be four X's followed by the last four digits. -->
					<xs:element name="creditCardNumberMasked" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:minLength value="8" />
								<xs:maxLength value="8" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<!-- Format of bankRoutingNumberMasked should be four X's followed by the last four digits. -->
					<xs:element name="bankRoutingNumberMasked" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:minLength value="8" />
								<xs:maxLength value="8" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<!-- Format of bankAccountNumberMasked should be four X's followed by the last four digits. -->
					<xs:element name="bankAccountNumberMasked" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:minLength value="8" />
								<xs:maxLength value="8" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<xs:element name="order" type="anet:orderExType" minOccurs="0" />
					<xs:element name="transId" type="anet:numericString" minOccurs="0" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransVoidType">
		<xs:sequence>
			<xs:element name="customerProfileId" type="anet:numericString" minOccurs="0" />
			<xs:element name="customerPaymentProfileId" type="anet:numericString" minOccurs="0" />
			<xs:element name="customerShippingAddressId" type="anet:numericString" minOccurs="0" />
			<xs:element name="transId" type="anet:numericString" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransactionType">
		<xs:choice>
			<xs:element name="profileTransAuthCapture" type="anet:profileTransAuthCaptureType" />
			<xs:element name="profileTransAuthOnly" type="anet:profileTransAuthOnlyType" />
			<xs:element name="profileTransPriorAuthCapture" type="anet:profileTransPriorAuthCaptureType" />
			<xs:element name="profileTransCaptureOnly" type="anet:profileTransCaptureOnlyType" />
			<xs:element name="profileTransRefund" type="anet:profileTransRefundType" />
			<xs:element name="profileTransVoid" type="anet:profileTransVoidType" />
		</xs:choice>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="transactionSummaryType">
		<xs:sequence>
			<xs:element name="transId" type="anet:numericString" />
			<xs:element name="submitTimeUTC" type="xs:dateTime" />
			<xs:element name="submitTimeLocal" type="xs:dateTime" />
			<xs:element name="transactionStatus" type="xs:string" /> <!-- anet:transactionStatusEnum -->
			<xs:element name="invoiceNumber" type="xs:string" minOccurs="0" />
			<xs:element name="firstName" type="xs:string" minOccurs="0" />
			<xs:element name="lastName" type="xs:string" minOccurs="0" />
			<xs:element name="accountType" type="xs:string" /> <!-- anet:accountTypeEnum -->
			<xs:element name="accountNumber" type="xs:string" />
			<xs:element name="settleAmount" type="xs:decimal" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="transactionDetailsType">
		<xs:sequence>
			<xs:element name="transId" type="anet:numericString" />
			<xs:element name="refTransId" type="anet:numericString" minOccurs="0" />
			<xs:element name="splitTenderId" type="anet:numericString" minOccurs="0" />
			<xs:element name="submitTimeUTC" type="xs:dateTime" />
			<xs:element name="submitTimeLocal" type="xs:dateTime" />
			<xs:element name="transactionType" type="xs:string" /> <!-- anet:transactionTypeEnum -->
			<xs:element name="transactionStatus" type="xs:string" /> <!-- anet:transactionStatusEnum -->
			<xs:element name="responseCode" type="xs:int" />
			<xs:element name="responseReasonCode" type="xs:int" />
			<xs:element name="responseReasonDescription" type="xs:string" />
			<xs:element name="authCode" minOccurs="0" >
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="6" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="AVSResponse" minOccurs="0" >
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="1" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="cardCodeResponse" minOccurs="0" >
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="1" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="CAVVResponse" minOccurs="0" >
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="1" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="FDSFilterAction" type="xs:string" minOccurs="0" /> <!-- anet:FDSFilterActionEnum -->
			<xs:element name="FDSFilters" type="anet:ArrayOfFDSFilter" minOccurs="0" />
			<xs:element name="batch" type="anet:batchDetailsType" minOccurs="0" />
			<xs:element name="order" type="anet:orderExType" minOccurs="0" />
			<xs:element name="requestedAmount" minOccurs="0" >
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.00" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="authAmount" >
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.00" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="settleAmount">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.00" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="tax" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="shipping" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="duty" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="lineItems" type="anet:ArrayOfLineItem" minOccurs="0" />
			<xs:element name="prepaidBalanceRemaining" minOccurs="0" >
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="taxExempt" type="xs:boolean" minOccurs="0" />
			<xs:element name="payment" type="anet:paymentMaskedType" />
			<xs:element name="customer" type="anet:customerDataType" minOccurs="0" />
			<xs:element name="billTo" type="anet:customerAddressType" minOccurs="0" />
			<xs:element name="shipTo" type="anet:nameAndAddressType" minOccurs="0" />
			<xs:element name="recurringBilling" type="xs:boolean" minOccurs="0" />
			<xs:element name="customerIP" type="xs:string" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="FDSFilterType">
		<xs:sequence>
			<xs:element name="name" type="xs:string" />
			<xs:element name="action" type="xs:string" /> <!-- anet:FDSFilterActionEnum -->
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="batchDetailsType">
		<xs:sequence>
			<xs:element name="batchId" type="anet:numericString" />
			<xs:element name="settlementTimeUTC" type="xs:dateTime" minOccurs="0" />
			<xs:element name="settlementTimeLocal" type="xs:dateTime" minOccurs="0" />
			<xs:element name="settlementState" type="xs:string" /> <!-- anet:settlementStateEnum -->
			<xs:element name="paymentMethod" type="xs:string" minOccurs="0" />  <!-- anet:paymentMethodEnum -->
			<xs:element name="statistics" type="anet:ArrayOfBatchStatisticType" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="batchStatisticType">
		<xs:sequence>
			<xs:element name="accountType" type="xs:string" /> <!-- anet:accountTypeEnum -->
			<xs:element name="chargeAmount" type="xs:decimal" />
			<xs:element name="chargeCount" type="xs:int" />
			<xs:element name="refundAmount" type="xs:decimal" />
			<xs:element name="refundCount" type="xs:int" />
			<xs:element name="voidCount" type="xs:int" />
			<xs:element name="declineCount" type="xs:int" />
			<xs:element name="errorCount" type="xs:int" />
			<xs:element name="returnedItemAmount" type="xs:decimal" minOccurs="0" maxOccurs="1" />
			<xs:element name="returnedItemCount" type="xs:int" minOccurs="0" />
			<xs:element name="chargebackAmount" type="xs:decimal" minOccurs="0" />
			<xs:element name="chargebackCount" type="xs:int" minOccurs="0" />
			<xs:element name="correctionNoticeCount" type="xs:int" minOccurs="0" />
			<xs:element name="chargeChargeBackAmount" type="xs:decimal" minOccurs="0" />
			<xs:element name="chargeChargeBackCount" type="xs:int" minOccurs="0" />
			<xs:element name="refundChargeBackAmount" type="xs:decimal" minOccurs="0" />
			<xs:element name="refundChargeBackCount" type="xs:int" minOccurs="0" />
			<xs:element name="chargeReturnedItemsAmount" type="xs:decimal" minOccurs="0" />
			<xs:element name="chargeReturnedItemsCount" type="xs:int" minOccurs="0" />
			<xs:element name="refundReturnedItemsAmount" type="xs:decimal" minOccurs="0" />
			<xs:element name="refundReturnedItemsCount" type="xs:int" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="transactionResponse">
		<xs:sequence>
			<xs:element name="responseCode" type="xs:string" minOccurs="0" />
			<xs:element name="authCode" type="xs:string" minOccurs="0" />
			<xs:element name="avsResultCode" type="xs:string" minOccurs="0" />
			<xs:element name="cvvResultCode" type="xs:string" minOccurs="0" />
			<xs:element name="cavvResultCode" type="xs:string" minOccurs="0" />
			<xs:element name="transId" type="xs:string" minOccurs="0" />
			<xs:element name="refTransID" type="xs:string" minOccurs="0" />
			<xs:element name="transHash" type="xs:string" minOccurs="0" />
			<xs:element name="testRequest" type="xs:string" minOccurs="0" />
			<xs:element name="accountNumber" type="xs:string" minOccurs="0" />
			<xs:element name="accountType" type="xs:string" minOccurs="0" />
			<xs:element name="splitTenderId" type="xs:string" minOccurs="0" />
			<xs:element name="prePaidCard" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="requestedAmount" type="xs:string" minOccurs="0" />
						<xs:element name="approvedAmount" type="xs:string" minOccurs="0" />
						<xs:element name="balanceOnCard" type="xs:string" minOccurs="0" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="messages" minOccurs="0">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="message" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="code" type="xs:string" minOccurs="0" />
									<xs:element name="description" type="xs:string" minOccurs="0" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="errors" minOccurs="0">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="error" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="errorCode" type="xs:string" minOccurs="0" />
									<xs:element name="errorText" type="xs:string" minOccurs="0" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="splitTenderPayments" minOccurs="0">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="splitTenderPayment" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="transId" type="xs:string" minOccurs="0" />
									<xs:element name="responseCode" type="xs:string" minOccurs="0" />
									<xs:element name="responseToCustomer" type="xs:string" minOccurs="0" />
									<xs:element name="authCode" type="xs:string" minOccurs="0" />
									<xs:element name="accountNumber" type="xs:string" minOccurs="0" />
									<xs:element name="accountType" type="xs:string" minOccurs="0" />
									<xs:element name="requestedAmount" type="xs:string" minOccurs="0" />
									<xs:element name="approvedAmount" type="xs:string" minOccurs="0" />
									<xs:element name="balanceOnCard" type="xs:string" minOccurs="0" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="userFields" minOccurs="0">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="userField" type="anet:userField" minOccurs="0" maxOccurs="20" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!--
	===================================================================
	The ANetApiRequest defines elements common to all API method
	requests.
	===================================================================
	-->
	<xs:complexType name="ANetApiRequest">
		<xs:sequence>
			<xs:element name="merchantAuthentication" type="anet:merchantAuthenticationType" />
			<xs:element name="refId" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!--
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	 Response type definitions begin here
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	-->
	<!--
	===================================================================
	The messagesType provides the result of the request. The resultCode
	element provides the overall result of the request. The individual
	message(s) provide more detail, especially for errors, about the result.

	Ok - The request was processed and accepted without error. If any
		messages are present they will be informational only.
	Error - The request resulted in one or more errors. See messages
		for details.
	===================================================================
	-->
	<xs:simpleType name="messageTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="Ok" />
			<xs:enumeration value="Error" />
		</xs:restriction>
	</xs:simpleType>
	<xs:complexType name="messagesType">
		<xs:sequence>
			<xs:element name="resultCode" type="anet:messageTypeEnum" />
			<xs:element name="message" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="code" type="xs:string" />
						<xs:element name="text" type="xs:string" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!--
	===================================================================
	The ANetApiResponse defines elements common to all API method
	responses.
	===================================================================
	-->
	<xs:complexType name="ANetApiResponse">
		<xs:sequence>
			<xs:element name="refId" type="xs:string" minOccurs="0" />
			<xs:sequence>
				<xs:element name="messages" type="anet:messagesType" />
			</xs:sequence>
			<xs:element name="sessionToken" type="xs:string" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
	</xs:complexType>
	<!--
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	 API method definitions begin here
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	-->
	<!--
	===================================================================
	errorResponse
	This is the response when an error occurs before the method can
	be determined, such as an "unknown method" type of error.
	===================================================================
	-->
	<xs:element name="ErrorResponse" type="anet:ANetApiResponse" />
	<!--
	===================================================================
	isAliveRequest
	This method is used to test the availability of the API.
	===================================================================
	-->
	<xs:element name="isAliveRequest">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="refId" minOccurs="0">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:maxLength value="20" />
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	isAliveResponse
	This is the response to isAliveRequest.
	===================================================================
	-->
	<xs:element name="isAliveResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	authenticateTestRequest
	This method is used to test the availability of the API.
	===================================================================
	-->
	<xs:element name="authenticateTestRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	authenticateTestResponse
	This is the response to authenticateTestRequest.
	===================================================================
	-->
	<xs:element name="authenticateTestResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	ARBCreateSubscriptionRequest
	This method is used to create a new ARB subscription.
	The merchant must be signed up for the ARB service to use it.
	===================================================================
	-->
	<xs:element name="ARBCreateSubscriptionRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="subscription" type="anet:ARBSubscriptionType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	ARBCreateSubscriptionResponse
	This is the response to ARBCreateSubscriptionRequest.
	===================================================================
	-->
	<xs:element name="ARBCreateSubscriptionResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- subscriptionId will only be present if a subscription was created. -->
						<xs:element name="subscriptionId" type="anet:numericString" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	ARBUpdateSubscriptionRequest
	This method is used to update an existing ARB subscription.
	The merchant must be signed up for the ARB service to use it.
	===================================================================
	-->
	<xs:element name="ARBUpdateSubscriptionRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="subscriptionId" type="anet:numericString" />
						<xs:element name="subscription" type="anet:ARBSubscriptionType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	ARBUpdateSubscriptionResponse
	This is the response to ARBUpdateSubscriptionResponse.
	===================================================================
	-->
	<xs:element name="ARBUpdateSubscriptionResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	ARBCancelSubscriptionRequest
	This method is used to cancel an existing ARB subscription.
	The merchant must be signed up for the ARB service to use it.
	===================================================================
	-->
	<xs:element name="ARBCancelSubscriptionRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="subscriptionId" type="anet:numericString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	ARBCancelSubscriptionResponse
	This is the response to ARBCancelSubscriptionRequest.
	===================================================================
	-->
	<xs:element name="ARBCancelSubscriptionResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	ARBGetSubscriptionStatusRequest
	This method is used to get the status of an existing ARB subscription.
	The merchant must be signed up for the ARB service to use it.
	===================================================================
	-->
	<xs:element name="ARBGetSubscriptionStatusRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="subscriptionId" type="anet:numericString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	ARBGetSubscriptionStatusResponse
	This is the response to ARBGetSubscriptionStatusRequest.
	===================================================================
	-->
	<xs:element name="ARBGetSubscriptionStatusResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element name="status" type="anet:ARBSubscriptionStatusEnum" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	createCustomerProfileRequest
	This method is used to create a new customer profile along with any
	customer payment profiles and customer shipping addresses for the customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
	<xs:element name="createCustomerProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="profile" type="anet:customerProfileType" />
						<xs:element name="validationMode" type="anet:validationModeEnum" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	createCustomerProfileResponse
	This is the response to createCustomerProfileRequest.
	===================================================================
	-->
	<xs:element name="createCustomerProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- customerProfileId will only be present if a profile was created. -->
						<xs:element name="customerProfileId" type="anet:numericString" minOccurs="0" />
						<xs:element name="customerPaymentProfileIdList" type="anet:ArrayOfNumericString" />
						<xs:element name="customerShippingAddressIdList" type="anet:ArrayOfNumericString" />
						<xs:element name="validationDirectResponseList" type="anet:ArrayOfString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	createCustomerPaymentProfileRequest
	This method is used to create a new customer payment profile for an existing customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
	<xs:element name="createCustomerPaymentProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="paymentProfile" type="anet:customerPaymentProfileType" />
						<xs:element name="validationMode" type="anet:validationModeEnum" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	createCustomerPaymentProfileResponse
	This is the response to createCustomerPaymentProfileRequest.
	===================================================================
	-->
	<xs:element name="createCustomerPaymentProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- customerPaymentProfileId will only be present if a payment profile was created. -->
						<xs:element name="customerPaymentProfileId" type="anet:numericString" minOccurs="0" />
						<!-- validationDirectResponse will only be present if validationMode is testMode or liveMode. -->
						<xs:element name="validationDirectResponse" minOccurs="0">
							<xs:simpleType>
								<xs:restriction base="xs:string">
									<xs:maxLength value="2048" />
								</xs:restriction>
							</xs:simpleType>
						</xs:element>
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	createCustomerShippingAddressRequest
	This method is used to create a new customer shipping address for an existing customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
	<xs:element name="createCustomerShippingAddressRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="address" type="anet:customerAddressType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	createCustomerShippingAddressResponse
	This is the response to createCustomerShippingAddressRequest.
	===================================================================
	-->
	<xs:element name="createCustomerShippingAddressResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- customerAddressId will only be present if a payment profile was created. -->
						<xs:element name="customerAddressId" type="anet:numericString" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getCustomerProfileRequest
	This method is used to retrieve an existing customer profile along with all the
	customer payment profiles and customer shipping addresses for the customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
	<xs:element name="getCustomerProfileRequest">
		<xs:complexType>
					<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="customerProfileId" type="anet:numericString" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	getCustomerProfileResponse
	This is the response to getCustomerProfileRequest.
	===================================================================
	-->
		<xs:element name="getCustomerProfileResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
										<xs:sequence>
												<!-- profile will only be present if a profile was successfully retrieved. -->
												<xs:element name="profile" type="anet:customerProfileMaskedType" minOccurs="0" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	getCustomerPaymentProfileRequest
	This method is used to retrieve an existing customer payment profile for a customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="getCustomerPaymentProfileRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="customerProfileId" type="anet:numericString" />
												<xs:element name="customerPaymentProfileId" type="anet:numericString" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	getCustomerPaymentProfileResponse
	This is the response to getCustomerPaymentProfileRequest.
	===================================================================
	-->
		<xs:element name="getCustomerPaymentProfileResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
										<xs:sequence>
												<!-- paymentProfile and customerProfileId will only be present if a payment profile was successfully retrieved. -->
												<xs:element name="paymentProfile" type="anet:customerPaymentProfileMaskedType" minOccurs="0" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	getCustomerShippingAddressRequest
	This method is used to retrieve an existing customer shipping address for a customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="getCustomerShippingAddressRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="customerProfileId" type="anet:numericString" />
												<xs:element name="customerAddressId" type="anet:numericString" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	getCustomerShippingAddressResponse
	This is the response to getCustomerShippingAddressRequest.
	===================================================================
	-->
		<xs:element name="getCustomerShippingAddressResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
										<xs:sequence>
												<!-- address and customerProfileId will only be present if a shipping address was successfully retrieved. -->
												<xs:element name="address" type="anet:customerAddressExType" minOccurs="0" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	updateCustomerProfileRequest
	This method is used to update an existing customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="updateCustomerProfileRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="profile" type="anet:customerProfileExType" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	updateCustomerProfileResponse
	This is the response to updateCustomerProfileRequest.
	===================================================================
	-->
		<xs:element name="updateCustomerProfileResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	updateCustomerPaymentProfileRequest
	This method is used to update an existing customer payment profile for a customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="updateCustomerPaymentProfileRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="customerProfileId" type="anet:numericString" />
												<xs:element name="paymentProfile" type="anet:customerPaymentProfileExType" />
												<xs:element name="validationMode" type="anet:validationModeEnum" minOccurs="0" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	updateCustomerPaymentProfileResponse
	This is the response to updateCustomerPaymentProfileRequest.
	===================================================================
	-->
		<xs:element name="updateCustomerPaymentProfileResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
										<xs:sequence>
												<!-- validationDirectResponse will only be present if validationMode is testMode or liveMode. -->
												<xs:element name="validationDirectResponse" minOccurs="0">
														<xs:simpleType>
																<xs:restriction base="xs:string">
																		<xs:maxLength value="2048" />
																</xs:restriction>
														</xs:simpleType>
												</xs:element>
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	updateCustomerShippingAddressRequest
	This method is used to update an existing customer shipping address for a customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="updateCustomerShippingAddressRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="customerProfileId" type="anet:numericString" />
												<xs:element name="address" type="anet:customerAddressExType" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	updateCustomerShippingAddressResponse
	This is the response to updateCustomerShippingAddressRequest.
	===================================================================
	-->
		<xs:element name="updateCustomerShippingAddressResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	deleteCustomerProfileRequest
	This method is used to delete an existing customer profile along with all the
	customer payment profiles and customer shipping addresses for the customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="deleteCustomerProfileRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="customerProfileId" type="anet:numericString" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	deleteCustomerProfileResponse
	This is the response to deleteCustomerProfileRequest.
	===================================================================
	-->
		<xs:element name="deleteCustomerProfileResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	deleteCustomerPaymentProfileRequest
	This method is used to delete an existing customer payment profile from a customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="deleteCustomerPaymentProfileRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="customerProfileId" type="anet:numericString" />
												<xs:element name="customerPaymentProfileId" type="anet:numericString" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	deleteCustomerPaymentProfileResponse
	This is the response to deleteCustomerPaymentProfileRequest.
	===================================================================
	-->
		<xs:element name="deleteCustomerPaymentProfileResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	deleteCustomerShippingAddressRequest
	This method is used to delete an existing customer shipping address from a customer profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="deleteCustomerShippingAddressRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="customerProfileId" type="anet:numericString" />
												<xs:element name="customerAddressId" type="anet:numericString" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	deleteCustomerShippingAddressResponse
	This is the response to deleteCustomerShippingAddressRequest.
	===================================================================
	-->
		<xs:element name="deleteCustomerShippingAddressResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	createCustomerProfileTransactionRequest
	This method is used to generate a payment transaction for a customer payment profile.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="createCustomerProfileTransactionRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="transaction" type="anet:profileTransactionType" />
												<xs:element name="extraOptions" minOccurs="0">
														<xs:simpleType>
																<xs:restriction base="xs:string">
																		<xs:maxLength value="1024" />
																</xs:restriction>
														</xs:simpleType>
												</xs:element>
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	createCustomerProfileTransactionResponse
	This is the response to createCustomerProfileTransactionRequest.
	===================================================================
	-->
		<xs:element name="createCustomerProfileTransactionResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
										<xs:sequence>
												<xs:element name="directResponse" minOccurs="0">
														<xs:simpleType>
																<xs:restriction base="xs:string">
																		<xs:maxLength value="2048" />
																</xs:restriction>
														</xs:simpleType>
												</xs:element>
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	validateCustomerPaymentProfileRequest
	This method is used to check a customer payment profile by generating a test transaction for it.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="validateCustomerPaymentProfileRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="customerProfileId" type="anet:numericString" />
												<xs:element name="customerPaymentProfileId" type="anet:numericString" />
												<xs:element name="customerShippingAddressId" type="anet:numericString" minOccurs="0" />
												<xs:element name="cardCode" minOccurs="0">
														<xs:simpleType>
																<xs:restriction base="anet:numericString">
																		<xs:minLength value="3" />
																		<xs:maxLength value="4" />
																</xs:restriction>
														</xs:simpleType>
												</xs:element>
												<xs:element name="validationMode" type="anet:validationModeEnum" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	validateCustomerPaymentProfileResponse
	This is the response to validateCustomerPaymentProfileRequest.
	===================================================================
	-->
		<xs:element name="validateCustomerPaymentProfileResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
										<xs:sequence>
												<xs:element name="directResponse" minOccurs="0">
														<xs:simpleType>
																<xs:restriction base="xs:string">
																		<xs:maxLength value="2048" />
																</xs:restriction>
														</xs:simpleType>
												</xs:element>
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	getCustomerProfileIdsRequest
	This method is used retrieve the customer profile ids for your account in case they get lost.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
		<xs:element name="getCustomerProfileIdsRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	getCustomerProfileIdsResponse
	This is the response to getCustomerProfileIdsRequest.
	===================================================================
	-->
		<xs:element name="getCustomerProfileIdsResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
										<xs:sequence>
												<xs:element name = "ids" type = "anet:ArrayOfNumericString" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	updateSplitTenderGroupRequest
	This method is used to void or release an order after getting a partial authorization for a transaction.
	===================================================================
	-->
		<xs:element name="updateSplitTenderGroupRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="splitTenderId" type="xs:string" />
												<xs:element name="splitTenderStatus" type="anet:splitTenderStatusEnum" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	updateSplitTenderGroupResponse
	This is the response to updateSplitTenderGroupRequest.
	===================================================================
	-->
		<xs:element name="updateSplitTenderGroupResponse">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiResponse">
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	getTransactionDetailsRequest
	This method is used to retrieve detailed information about a single transaction.
	===================================================================
	-->
		<xs:element name="getTransactionDetailsRequest">
				<xs:complexType>
						<xs:complexContent>
								<xs:extension base="anet:ANetApiRequest">
										<xs:sequence>
												<xs:element name="transId" type="anet:numericString" />
										</xs:sequence>
								</xs:extension>
						</xs:complexContent>
				</xs:complexType>
		</xs:element>
		<!--
	===================================================================
	getTransactionDetailsResponse
	This is the response to getTransactionDetailsRequest.
	===================================================================
	-->
	<xs:element name="getTransactionDetailsResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element name="transaction" type="anet:transactionDetailsType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	createTransactionRequest
	This method is used to process transactions.
	===================================================================
	-->
	<xs:element name="createTransactionRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="transactionRequest" type="anet:transactionRequestType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	createTransactionResponse
	This is the response that will be returned to a client following
	any type of transaction request.
	===================================================================
		-->
	<xs:element name="createTransactionResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element name="transactionResponse" type="anet:transactionResponse" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getBatchStatisticsRequest
	This method is used to get the batch details for the specified BatchId
	===================================================================
	-->
	<xs:element name="getBatchStatisticsRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="batchId" type="anet:numericString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getBatchStatisticsResponse
	This is the response to getBatchStatisticsRequest.
	===================================================================
	-->
	<xs:element name="getBatchStatisticsResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element minOccurs="0" maxOccurs="unbounded" name="batch" type="anet:batchDetailsType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getSettledBatchListRequest
	This method is used to retrieve a list of settled batches.
	===================================================================
	-->
	<xs:element name="getSettledBatchListRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="includeStatistics" type="xs:boolean" minOccurs="0" />
						<xs:element name="firstSettlementDate" type="xs:dateTime" minOccurs="0" />
						<xs:element name="lastSettlementDate" type="xs:dateTime" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getSettledBatchListResponse
	This is the response to getSettledBatchListRequest.
	===================================================================
	-->
	<xs:element name="getSettledBatchListResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element name="batchList" type="anet:ArrayOfBatchDetailsType" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getTransactionListRequest
	This method is used to retrieve a list of settled transactions.
	===================================================================
	-->
	<xs:element name="getTransactionListRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="batchId" type="anet:numericString" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getTransactionListResponse
	This is the response to getTransactionListRequest.
	===================================================================
	-->
	<xs:element name="getTransactionListResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element name="transactions" type="anet:ArrayOfTransactionSummaryType" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getHostedProfilePageRequest
	This method is used to give access to the hosted customer profile page to one of your customers.
	The merchant must be signed up for the CIM service to use it.
	===================================================================
	-->
	<xs:element name="getHostedProfilePageRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="hostedProfileSettings" type="anet:ArrayOfSetting" minOccurs="0">
							<xs:annotation>
								<xs:documentation>Allowed values for settingName are: hostedProfileReturnUrl, hostedProfileReturnUrlText, hostedProfilePageBorderVisible, hostedProfileIFrameCommunicatorUrl, hostedProfileHeadingBgColor.</xs:documentation>
							</xs:annotation>
						</xs:element>
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getHostedProfilePageResponse
	This is the response to getHostedProfilePageRequest.
	===================================================================
	-->
	<xs:element name="getHostedProfilePageResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element name="token" type="xs:string" />
					</xs:sequence>
				</xs:extension>
		</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getUnsettledTransactionListRequest
	This method is used to retrieve a list of unsettled transactions.
	===================================================================
	-->
	<xs:element name="getUnsettledTransactionListRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	getUnsettledTransactionListResponse
	This is the response to getUnsettledTransactionListRequest.
	===================================================================
	-->
	<xs:element name="getUnsettledTransactionListResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element name="transactions" type="anet:ArrayOfTransactionSummaryType" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>

<!--
	===================================================================
	mobileDeviceRegistrationRequest
	This method is used to request registration for a mobile device.
	===================================================================
	-->
	<xs:element name="mobileDeviceRegistrationRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="mobileDevice" type="anet:mobileDeviceType" minOccurs="1" maxOccurs="1" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	mobileDeviceRegistrationResponse
	This is the response to mobileDeviceRegistrationRequest.
	===================================================================
	-->
	<xs:element name="mobileDeviceRegistrationResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse" />
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	mobileDeviceLoginRequest
	This method is used to authenticate a mobile device.
	===================================================================
	-->
	<xs:element name="mobileDeviceLoginRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest" />
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	mobileDeviceLoginResponse
	This is the response to mobileDeviceLoginRequest.
	===================================================================
	-->
	<xs:element name="mobileDeviceLoginResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element name="merchantContact" type="anet:merchantContactType" />
						<xs:element name="userPermissions" type="anet:ArrayOfPermissionType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	logoutRequest
	This method is used to end a session from a mobile device.
	===================================================================
	-->
	<xs:element name="logoutRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest" />
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	logoutResponse
	This is the response to logoutRequest.
	===================================================================
	-->
	<xs:element name="logoutResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse" />
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	sendCustomerTransactionReceiptRequest
	This method is used to send a transaction email receipt.
	===================================================================
	-->
	<xs:element name="sendCustomerTransactionReceiptRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="transId" type="anet:numericString" />
						<xs:element name="customerEmail" type="xs:string" />
						<xs:element name="emailSettings" type="anet:ArrayOfSetting" minOccurs="0">
							<xs:annotation>
								<xs:documentation>Allowed values for settingName are: headerEmailReceipt and footerEmailReceipt</xs:documentation>
							</xs:annotation>
						</xs:element>
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!--
	===================================================================
	sendCustomerTransactionReceiptResponse
	This is the response to sendCustomerTransactionReceiptRequest.
	===================================================================
	-->
	<xs:element name="sendCustomerTransactionReceiptResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse" />
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
</xs:schema>
"""
