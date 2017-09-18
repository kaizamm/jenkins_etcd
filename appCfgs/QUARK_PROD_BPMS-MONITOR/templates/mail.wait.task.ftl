<p><strong>${title}</strong><br/>
<br />
<#if waitTaskList?? && (waitTaskList?size > 0)>
	<table style="border: black solid 1px;" cellpadding="0" border="1" cellspacing="0" >
		<thead style="background-color: cornflowerblue;">
			<tr>
				<th>&nbsp; No. &nbsp;</div></th>
				<th>&nbsp; Task ID &nbsp;</th>
				<th>&nbsp;&nbsp; Total &nbsp;&nbsp;</th>
			</tr>
		</thead>
		<#list waitTaskList as item>
			<tr style="text-align: center">
			  <td>${item_index + 1}</td>
			  <td>${item.actId!''}</td>
			  <td>${item.count!''}</td>
			</tr>
		</#list>
	</table>
<#else>
	<p style="margin: 20px; color: #F08080">目前没有正在等待的节点。</p>
</#if>
